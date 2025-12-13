from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from database.requests import set_user
from keyboards.builders import main_kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await set_user(message.from_user.id, message.from_user.username)
    await message.answer(
        "👋 <b>Привет! Я Трекер Привычек.</b>\n\n"
        "Я помогу тебе выстроить дисциплину и не потерять «огонек» прогресса.\n"
        "Начни с кнопки <b>«Новая привычка»</b>.",
        reply_markup=main_kb(),
        parse_mode="HTML"
    )