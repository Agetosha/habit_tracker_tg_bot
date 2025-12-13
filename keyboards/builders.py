from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def main_kb():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="➕ Новая привычка"), KeyboardButton(text="✅ Отметить выполнение")],
            [KeyboardButton(text="📊 Моя статистика"), KeyboardButton(text="🔥 Мои привычки")]
        ],
        resize_keyboard=True,
        input_field_placeholder="Выберите действие..."
    )

def habits_inline_kb(habits, action_type="track"):
    # action_type: "track" (отметить) или "stats" (статистика)
    builder = InlineKeyboardBuilder()
    for habit in habits:
        callback_data = f"{action_type}_{habit.id}"
        builder.add(InlineKeyboardButton(
            text=f"{habit.title} (🔥{habit.current_streak})", 
            callback_data=callback_data
        ))
    builder.adjust(1) # По 1 кнопке в ряд
    return builder.as_markup()