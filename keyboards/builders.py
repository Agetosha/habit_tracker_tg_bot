from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def main_kb():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="➕ Новая привычка"), KeyboardButton(text="✅ Отметить")],
            [KeyboardButton(text="📊 Статистика"), KeyboardButton(text="🗑 Удалить привычку")],
            [KeyboardButton(text="🔥 Мои привычки")]
        ],
        resize_keyboard=True,
        input_field_placeholder="Выберите действие..."
    )

# Новая клавиатура для процесса создания
def cancel_kb():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="❌ Отмена")]
        ],
        resize_keyboard=True,
        input_field_placeholder="Напишите название или отмените..."
    )

def habits_inline_kb(habits, action_type="track"):
    builder = InlineKeyboardBuilder()
    for habit in habits:
        callback_data = f"{action_type}_{habit.id}"
        builder.add(InlineKeyboardButton(
            text=f"{habit.title}", 
            callback_data=callback_data
        ))
    builder.adjust(1)
    return builder.as_markup()