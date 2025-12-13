from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, BufferedInputFile
from database.requests import get_user_habits, get_habit_logs
from keyboards.builders import habits_inline_kb
from services.stats_gen import generate_habit_chart

router = Router()

@router.message(F.text == "📊 Моя статистика")
async def select_stat_habit(message: Message):
    habits = await get_user_habits(message.from_user.id)
    if not habits:
        await message.answer("Нет данных для статистики.")
        return
    await message.answer("Выберите привычку для отчета:", reply_markup=habits_inline_kb(habits, "stats"))

@router.callback_query(F.data.startswith("stats_"))
async def show_chart(callback: CallbackQuery):
    habit_id = int(callback.data.split("_")[1])
    
    # Получаем данные
    logs = await get_habit_logs(habit_id)
    
    # Нужно найти название привычки (можно оптимизировать запрос, но сделаем перебором для простоты примера)
    # В реальном проекте лучше сделать отдельный SELECT
    habits = await get_user_habits(callback.from_user.id)
    habit_title = next((h.title for h in habits if h.id == habit_id), "Привычка")
    
    # Генерируем картинку
    image_buf = generate_habit_chart(habit_title, logs)
    
    if image_buf:
        photo = BufferedInputFile(image_buf.read(), filename="chart.png")
        await callback.message.answer_photo(photo, caption=f"📈 Динамика: {habit_title}")
    else:
        await callback.message.answer("Недостаточно данных для графика.")
    
    await callback.answer()