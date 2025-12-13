from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from database.requests import get_user_habits, log_habit_completion
from keyboards.builders import habits_inline_kb
from services.api_quote import get_motivation_quote

router = Router()

class TrackState(StatesGroup):
    minutes = State()
    habit_id = State()

@router.message(F.text == "🔥 Мои привычки")
async def list_habits(message: Message):
    habits = await get_user_habits(message.from_user.id)
    if not habits:
        await message.answer("Список пуст. Создайте привычку!")
        return
    text = "<b>Ваши привычки и стрики:</b>\n"
    for h in habits:
        text += f"• {h.title}: {h.current_streak} дн. (Рекорд: {h.longest_streak})\n"
    await message.answer(text, parse_mode="HTML")

@router.message(F.text == "✅ Отметить выполнение")
async def select_habit_to_track(message: Message):
    habits = await get_user_habits(message.from_user.id)
    if not habits:
        await message.answer("Сначала создайте привычку!")
        return
    await message.answer("Выберите привычку:", reply_markup=habits_inline_kb(habits, "track"))

@router.callback_query(F.data.startswith("track_"))
async def ask_minutes(callback: CallbackQuery, state: FSMContext):
    habit_id = int(callback.data.split("_")[1])
    await state.update_data(habit_id=habit_id)
    await state.set_state(TrackState.minutes)
    await callback.message.answer("⏱ Сколько минут вы уделили этому сегодня? (введите число)")
    await callback.answer()

@router.message(TrackState.minutes)
async def save_track(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Введите число!")
        return
    
    minutes = int(message.text)
    data = await state.get_data()
    
    # Сохраняем и получаем новый стрик
    new_streak = await log_habit_completion(data['habit_id'], minutes)
    
    # Получаем мотивацию (Внешнее API)
    quote = await get_motivation_quote()
    
    await message.answer(
        f"✅ Отлично! Прогресс записан.\n"
        f"🔥 Твой текущий стрик: <b>{new_streak} дн.</b>\n\n"
        f"{quote}", 
        parse_mode="HTML"
    )
    await state.clear()