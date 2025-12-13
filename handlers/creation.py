from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from database.requests import add_habit

router = Router()

class HabitState(StatesGroup):
    title = State()
    description = State()

@router.message(F.text == "➕ Новая привычка")
async def start_creation(message: Message, state: FSMContext):
    await state.set_state(HabitState.title)
    await message.answer("📝 Введите название привычки (например: <i>Чтение, Бег</i>):", parse_mode="HTML")

@router.message(HabitState.title)
async def process_title(message: Message, state: FSMContext):
    await state.update_data(title=message.text)
    await state.set_state(HabitState.description)
    await message.answer("💬 Опишите цель (например: <i>30 минут в день</i>) или напишите 'нет':")

@router.message(HabitState.description)
async def process_desc(message: Message, state: FSMContext):
    data = await state.get_data()
    description = message.text if message.text.lower() != 'нет' else ""
    
    await add_habit(message.from_user.id, data['title'], description)
    await message.answer("✅ Привычка успешно создана! Начни выполнять её сегодня.", parse_mode="HTML")
    await state.clear()