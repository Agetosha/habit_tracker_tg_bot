from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from database.requests import get_user_habits, log_habit_completion, delete_habit
from keyboards.builders import habits_inline_kb
from services.api_quote import get_motivation_quote

router = Router()

class TrackState(StatesGroup):
    minutes = State()
    habit_id = State()

# --- СПИСОК ПРИВЫЧЕК ---
@router.message(F.text == "🔥 Мои привычки")
async def list_habits(message: Message):
    habits = await get_user_habits(message.from_user.id)
    if not habits:
        await message.answer("Список пуст. Создайте привычку!")
        return
    
    text = "<b>Ваши привычки:</b>\n\n"
    for h in habits:
        desc = f" ({h.description})" if h.description else ""
        text += f"🔹 <b>{h.title}</b>{desc}\n"
        text += f"   🔥 Стрик: {h.current_streak} | 🏆 Рекорд: {h.longest_streak}\n\n"
    
    await message.answer(text, parse_mode="HTML")

# --- ОТМЕТКА ВЫПОЛНЕНИЯ ---
@router.message(F.text.in_({"✅ Отметить", "✅ Отметить выполнение"}))
async def select_habit_to_track(message: Message):
    habits = await get_user_habits(message.from_user.id)
    if not habits:
        await message.answer("Сначала создайте привычку!")
        return
    await message.answer("Выберите привычку для отметки:", reply_markup=habits_inline_kb(habits, "track"))

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
        await message.answer("Пожалуйста, введите число (минуты)!")
        return
    
    minutes = int(message.text)
    data = await state.get_data()
    
    # 1. Записываем в БД
    new_streak = await log_habit_completion(data['habit_id'], minutes)
    
    # 2. Получаем цитату (API)
    quote = await get_motivation_quote()
    
    await message.answer(
        f"✅ <b>Прогресс записан!</b>\n"
        f"🔥 Твой текущий стрик: <b>{new_streak} дн.</b>\n\n"
        f"{quote}", 
        parse_mode="HTML"
    )
    await state.clear()

# --- УДАЛЕНИЕ ---
@router.message(F.text == "🗑 Удалить привычку")
async def select_habit_to_delete(message: Message):
    habits = await get_user_habits(message.from_user.id)
    if not habits:
        await message.answer("Список пуст.")
        return
    await message.answer("Выберите привычку, которую хотите удалить:", reply_markup=habits_inline_kb(habits, "delete"))

@router.callback_query(F.data.startswith("delete_"))
async def process_delete(callback: CallbackQuery):
    habit_id = int(callback.data.split("_")[1])
    is_deleted = await delete_habit(habit_id)
    
    if is_deleted:
        await callback.message.edit_text("❌ Привычка удалена.")
    else:
        await callback.message.edit_text("⚠ Ошибка при удалении.")
    await callback.answer()