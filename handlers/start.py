from aiogram import Router, F  # роутер и фильтры
from aiogram.types import Message  # тип сообщения

# фильтры команд aiogram
from aiogram.filters import CommandStart  # фильтр команды /start

# модули проекта
from database.requests import set_user  # функция регистрации пользователя
from keyboards.builders import main_kb  # главное меню клавиатуры
router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    # обработчик команды /start
    await set_user(message.from_user.id, message.from_user.username)
    await message.answer(
        "👋 <b>Привет! Я Трекер Привычек.</b>\n\n"
        "Я помогу тебе выстроить дисциплину и не потерять «огонек» прогресса.\n"
        "Начни с кнопки <b>«Новая привычка»</b>.",
        reply_markup=main_kb(),
        parse_mode="HTML"
    )