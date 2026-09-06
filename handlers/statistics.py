# роутер для маршрутизации и магический фильтр для условий
from aiogram import Router, F
# типы сообщений и файлов
from aiogram.types import Message, CallbackQuery, BufferedInputFile

# внутренние модули проекта 
from database.requests import get_user_habits, get_habit_logs# функции работы с базой данных
from keyboards.builders import habits_inline_kb# создание инлайн-клавиатур
from services.stats_gen import generate_habit_chart# генерация графиков статистики
from datetime import datetime

router = Router()

@router.message(F.text == "📊 Статистика")
async def select_stat_habit(message: Message):
    # обработка запроса на просмотр статистики
    habits = await get_user_habits(message.from_user.id)
    if not habits:
        await message.answer("Нет данных для статистики. Сначала создайте и выполните привычку.")
        return
    await message.answer("Выберите привычку, по которой хотите увидеть динамику:", reply_markup=habits_inline_kb(habits, "stats"))

@router.callback_query(F.data.startswith("stats_"))
async def show_chart(callback: CallbackQuery):
    # обработка выбора привычки для показа статистики
    # убираем старые инлайн-кнопки, редактируя сообщение
    await callback.message.edit_text(callback.message.text) 
    
    try:
        habit_id = int(callback.data.split("_")[1])  # извлекаем id привычки из callback данных
    except ValueError:
        await callback.message.answer("⚠ Ошибка: Неверный ID привычки.")
        await callback.answer()
        return

    # получаем данные о выполнении привычки из базы данных
    logs = await get_habit_logs(habit_id)
    
    # ищем название привычки для заголовка графика
    habits = await get_user_habits(callback.from_user.id)
    habit_title = next((h.title for h in habits if h.id == habit_id), "Привычка")
    
    if not logs:
        # если нет записей о выполнении, сообщаем об этом
        await callback.message.answer(f"🚫 У привычки **{habit_title}** нет записей за период, чтобы построить график.", parse_mode="Markdown")
        await callback.answer()
        return

    # генерируем график прогресса по привычке
    image_buf = generate_habit_chart(habit_title, logs)
    
    if image_buf:
        # создаем объект фотографии из буфера
        photo = BufferedInputFile(image_buf.read(), filename=f"{habit_title}_chart.png")
        
        # рассчитываем базовую статистику
        total_minutes = sum(log.minutes_spent for log in logs)  # общее количество минут
        log_days = len({log.date_logged.date() for log in logs})  # количество дней с записями
        avg_minutes = round(total_minutes / log_days) if log_days else 0  # среднее время в день

        # формируем подпись к графику
        caption = (
            f"📈 **Отчет по привычке: {habit_title}**\n\n"
            f"— Всего минут: **{total_minutes}**\n"
            f"— Дней с записью: **{log_days}**\n"
            f"— Среднее время в день: **{avg_minutes} мин.**"
        )
        
        # отправляем график с подписью
        await callback.message.answer_photo(photo, caption=caption, parse_mode="Markdown")
    else:
        # резервный вариант на случай ошибки генерации графика
        await callback.message.answer("Не удалось сгенерировать график.")
    
    # отправляем уведомление об успешном выполнении
    await callback.answer("График готов!")