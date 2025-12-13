from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from database.requests import add_habit
from keyboards.builders import main_kb, cancel_kb # Импортируем новую клавиатуру

router = Router()

class HabitState(StatesGroup):
    title = State()
    description = State()

# --- ЛОГИКА ОТМЕНЫ (должна быть выше остальных хендлеров state) ---
@router.message(F.text.casefold() == "❌ отмена")
@router.message(F.text.casefold() == "отмена")
async def cancel_handler(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    
    await state.clear()
    await message.answer("❌ Создание привычки отменено.", reply_markup=main_kb())

# --- НАЧАЛО СОЗДАНИЯ ---
@router.message(F.text == "➕ Новая привычка")
async def start_creation(message: Message, state: FSMContext):
    await state.set_state(HabitState.title)
    # Добавляем клавиатуру с кнопкой отмены
    await message.answer(
        "📝 Введите название привычки (например: <i>Чтение, Бег</i>):", 
        parse_mode="HTML",
        reply_markup=cancel_kb() 
    )

# --- ВВОД НАЗВАНИЯ ---
@router.message(HabitState.title)
async def process_title(message: Message, state: FSMContext):
    await state.update_data(title=message.text)
    await state.set_state(HabitState.description)
    await message.answer(
        "💬 Опишите цель (например: <i>30 минут в день</i>) или напишите 'нет':",
        reply_markup=cancel_kb()
    )

# --- ВВОД ОПИСАНИЯ И СОХРАНЕНИЕ ---
@router.message(HabitState.description)
async def process_desc(message: Message, state: FSMContext):
    data = await state.get_data()
    description = message.text if message.text.lower() != 'нет' else ""
    
    await add_habit(message.from_user.id, data['title'], description)
    # Возвращаем главную клавиатуру
    await message.answer(
        "✅ Привычка успешно создана! Начни выполнять её сегодня.", 
        parse_mode="HTML",
        reply_markup=main_kb()
    )
    await state.clear()