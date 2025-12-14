# типы клавиатур и кнопок aiogram
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# утилиты для построения клавиатур
from aiogram.utils.keyboard import InlineKeyboardBuilder

def main_kb():
    # главная клавиатура с основными действиями
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="➕ Новая привычка"), KeyboardButton(text="✅ Отметить")],
            [KeyboardButton(text="📊 Статистика"), KeyboardButton(text="🗑 Удалить привычку")],
            [KeyboardButton(text="🔥 Мои привычки")]
        ],
        resize_keyboard=True,  # подстраивается под размер экрана
        input_field_placeholder="Выберите действие..."
    )

def cancel_kb():
    # клавиатура для отмены действий
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="❌ Отмена")]
        ],
        resize_keyboard=True,
        input_field_placeholder="Напишите название или отмените..."
    )

def habits_inline_kb(habits, action_type="track"):
    # создаем инлайн-клавиатуру со списком привычек
    builder = InlineKeyboardBuilder()
    for habit in habits:
        callback_data = f"{action_type}_{habit.id}"
        builder.add(InlineKeyboardButton(
            text=f"{habit.title}", 
            callback_data=callback_data
        ))
    builder.adjust(1)  # размещаем кнопки по одной в строке
    return builder.as_markup()