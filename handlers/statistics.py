from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, BufferedInputFile
from database.requests import get_user_habits, get_habit_logs
from keyboards.builders import habits_inline_kb
from services.stats_gen import generate_habit_chart
from datetime import datetime

router = Router()

@router.message(F.text == "📊 Статистика")
async def select_stat_habit(message: Message):
    habits = await get_user_habits(message.from_user.id)
    if not habits:
        await message.answer("Нет данных для статистики. Сначала создайте и выполните привычку.")
        return
    await message.answer("Выберите привычку, по которой хотите увидеть динамику:", reply_markup=habits_inline_kb(habits, "stats"))

@router.callback_query(F.data.startswith("stats_"))
async def show_chart(callback: CallbackQuery):
    # Убираем старые инлайн-кнопки
    await callback.message.edit_text(callback.message.text) 
    
    try:
        habit_id = int(callback.data.split("_")[1])
    except ValueError:
        await callback.message.answer("⚠ Ошибка: Неверный ID привычки.")
        await callback.answer()
        return

    # Получаем данные
    logs = await get_habit_logs(habit_id)
    
    # Ищем название привычки для заголовка
    habits = await get_user_habits(callback.from_user.id)
    habit_title = next((h.title for h in habits if h.id == habit_id), "Привычка")
    
    if not logs:
        await callback.message.answer(f"🚫 У привычки **{habit_title}** нет записей за период, чтобы построить график.", parse_mode="Markdown")
        await callback.answer()
        return

    # Генерируем картинку 
    image_buf = generate_habit_chart(habit_title, logs)
    
    if image_buf:
        photo = BufferedInputFile(image_buf.read(), filename=f"{habit_title}_chart.png")
        
        # Расчет базовой статистики
        total_minutes = sum(log.minutes_spent for log in logs)
        log_days = len({log.date_logged.date() for log in logs})
        avg_minutes = round(total_minutes / log_days) if log_days else 0

        caption = (
            f"📈 **Отчет по привычке: {habit_title}**\n\n"
            f"— Всего минут: **{total_minutes}**\n"
            f"— Дней с записью: **{log_days}**\n"
            f"— Среднее время в день: **{avg_minutes} мин.**"
        )
        
        await callback.message.answer_photo(photo, caption=caption, parse_mode="Markdown")
    else:
        # Это не должно случиться, так как мы проверили logs, но на всякий случай
        await callback.message.answer("Не удалось сгенерировать график.")
    
    await callback.answer("График готов!") # Уведомление об успешном выполнении