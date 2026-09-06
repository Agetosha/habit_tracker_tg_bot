# импорт моделей и сессии из нашего модуля models.py
from database.models import async_session, User, Habit, HabitLog
# sqlalchemy - для работы с базой данных
from sqlalchemy import select  # конструктор SQL запросов SELECT
from datetime import datetime

async def set_user(tg_id, username):
    # добавляем нового пользователя в базу данных, если его еще нет
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        if not user:
            session.add(User(tg_id=tg_id, username=username))
            await session.commit()

async def add_habit(tg_id, title, description):
    # добавляем новую привычку для пользователя
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        if user:
            session.add(Habit(user_id=user.id, title=title, description=description))
            await session.commit()

async def get_user_habits(tg_id):
    # получаем все привычки пользователя
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        if not user: return []
        # используем scalars().all() для получения списка объектов
        result = await session.execute(select(Habit).where(Habit.user_id == user.id))
        return result.scalars().all()

async def log_habit_completion(habit_id, minutes):
    # записываем выполнение привычки и обновляем стрик
    async with async_session() as session:
        habit = await session.get(Habit, habit_id)
        if habit:
            # получаем последнюю запись о выполнении
            last_log = await session.scalar(
                select(HabitLog)
                .where(HabitLog.habit_id == habit_id)
                .order_by(HabitLog.date_logged.desc())
            )
            
            # логика обновления стрика
            if last_log:
                delta = datetime.now().date() - last_log.date_logged.date()  # сравниваем только даты
                if delta.days == 0:
                    pass  # уже отмечали сегодня
                elif delta.days == 1:
                    habit.current_streak += 1  # последовательные дни
                else:
                    habit.current_streak = 1  # пропустили день, сбрасываем
            else:
                habit.current_streak = 1  # первое выполнение

            # обновляем рекордную серию
            if habit.current_streak > habit.longest_streak:
                habit.longest_streak = habit.current_streak
            
            # обновляем общее время
            habit.total_minutes += minutes
            # создаем новую запись в логах
            session.add(HabitLog(habit_id=habit_id, minutes_spent=minutes))
            
            # сохраняем значение стрика до коммита, чтобы вернуть его
            current_streak_value = habit.current_streak
            
            await session.commit()
            return current_streak_value
        return 0

async def get_habit_logs(habit_id):
    # получаем все записи о выполнении для конкретной привычки
    async with async_session() as session:
        result = await session.execute(select(HabitLog).where(HabitLog.habit_id == habit_id))
        return result.scalars().all()

async def delete_habit(habit_id):
    # удаляем привычку по ее идентификатору
    async with async_session() as session:
        habit = await session.get(Habit, habit_id)
        if habit:
            await session.delete(habit)
            await session.commit()
            return True
        return False