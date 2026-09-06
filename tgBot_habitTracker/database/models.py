# sqlalchemy - библиотека для работы с базами данных (ORM)
from sqlalchemy import BigInteger, String, ForeignKey, DateTime, Integer  # типы данных SQL
# sqlalchemy.orm - система объектно-реляционного отображения
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship  # базовые классы и связи
# sqlalchemy.ext.asyncio - асинхронная работа с БД
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from datetime import datetime
from config import DB_URL

# создаем асинхронный движок для работы с базой данных
engine = create_async_engine(DB_URL, echo=True)
async_session = async_sessionmaker(engine)

class Base(AsyncAttrs, DeclarativeBase):
    # базовый класс для всех моделей с поддержкой асинхронности
    pass

class User(Base):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int] = mapped_column(BigInteger, unique=True)  # уникальный идентификатор пользователя в телеграме
    username: Mapped[str] = mapped_column(String, nullable=True)  # имя пользователя может быть пустым
    joined_at: Mapped[datetime] = mapped_column(default=datetime.now)  # дата регистрации

    # связь с привычками пользователя, при удалении пользователя удаляются все его привычки
    habits = relationship("Habit", back_populates="user", cascade="all, delete-orphan")

class Habit(Base):
    __tablename__ = 'habits'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))  # ссылка на пользователя
    title: Mapped[str] = mapped_column(String(100))  # название привычки (максимум 100 символов)
    description: Mapped[str] = mapped_column(String(255), nullable=True)  # описание (необязательное)
    current_streak: Mapped[int] = mapped_column(Integer, default=0)  # текущая серия выполнения
    longest_streak: Mapped[int] = mapped_column(Integer, default=0)  # самая длинная серия
    total_minutes: Mapped[int] = mapped_column(Integer, default=0)  # общее количество минут
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)  # дата создания привычки

    user = relationship("User", back_populates="habits")  # связь с пользователем
    
    # связь с логами выполнения, при удалении привычки удаляются все её логи
    logs = relationship("HabitLog", back_populates="habit", cascade="all, delete-orphan")

class HabitLog(Base):
    __tablename__ = 'habit_logs'

    id: Mapped[int] = mapped_column(primary_key=True)
    habit_id: Mapped[int] = mapped_column(ForeignKey('habits.id'), nullable=False)  # ссылка на привычку
    date_logged: Mapped[datetime] = mapped_column(default=datetime.now)  # дата отметки выполнения
    minutes_spent: Mapped[int] = mapped_column(Integer, default=0)  # сколько минут потрачено
    
    habit = relationship("Habit", back_populates="logs")  # связь с привычкой

async def async_main():
    # создаем все таблицы в базе данных
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)