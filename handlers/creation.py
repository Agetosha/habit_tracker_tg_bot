from aiogram import Router, F  # роутер для маршрутизации и фильтры условий
from aiogram.types import Message  # тип текстового сообщения

# aiogram.fsm - конечный автомат (машина состояний)
from aiogram.fsm.context import FSMContext  # контекст для управления состояниями
from aiogram.fsm.state import State, StatesGroup  # классы состояний

# модули проекта
from database.requests import add_habit  # функция добавления привычки в БД
from keyboards.builders import main_kb, cancel_kb  # клавиатуры (главная и отмена)

router = Router()

class HabitState(StatesGroup):
    # состояния конечного автомата для создания привычки
    title = State()  # состояние ввода названия
    description = State()  # состояние ввода описания

@router.message(F.text.casefold() == "❌ отмена")
@router.message(F.text.casefold() == "отмена")
async def cancel_handler(message: Message, state: FSMContext):
    # обработчик отмены создания привычки
    current_state = await state.get_state()
    if current_state is None:
        return
    
    await state.clear()  # сбрасываем состояние
    await message.answer("❌ Создание привычки отменено.", reply_markup=main_kb())

@router.message(F.text == "➕ Новая привычка")
async def start_creation(message: Message, state: FSMContext):
    # начало процесса создания привычки
    await state.set_state(HabitState.title)
    await message.answer(
        "📝 Введите название привычки (например: <i>Чтение, Бег</i>):", 
        parse_mode="HTML",
        reply_markup=cancel_kb()  # показываем клавиатуру с отменой
    )

@router.message(HabitState.title)
async def process_title(message: Message, state: FSMContext):
    # обработка введенного названия привычки
    await state.update_data(title=message.text)
    await state.set_state(HabitState.description)
    await message.answer(
        "💬 Опишите цель (например: 30 минут в день) или напишите 'нет':",
        reply_markup=cancel_kb()
    )

@router.message(HabitState.description)
async def process_desc(message: Message, state: FSMContext):
    # обработка описания и сохранение привычки
    data = await state.get_data()
    description = message.text if message.text.lower() != 'нет' else ""
    
    await add_habit(message.from_user.id, data['title'], description)
    await message.answer(
        "✅ Привычка успешно создана! Начни выполнять её сегодня.", 
        parse_mode="HTML",
        reply_markup=main_kb()  # возвращаем главную клавиатуру
    )
    await state.clear()  # очищаем состояние