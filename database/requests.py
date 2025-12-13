from database.models import async_session, User, Habit, HabitLog
from sqlalchemy import select, update, func
from datetime import datetime, timedelta

async def set_user(tg_id, username):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        if not user:
            session.add(User(tg_id=tg_id, username=username))
            await session.commit()

async def add_habit(tg_id, title, description):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        if user:
            session.add(Habit(user_id=user.id, title=title, description=description))
            await session.commit()

async def get_user_habits(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        if not user: return []
        result = await session.execute(select(Habit).where(Habit.user_id == user.id))
        return result.scalars().all()

async def log_habit_completion(habit_id, minutes):
    async with async_session() as session:
        habit = await session.get(Habit, habit_id)
        if habit:
            # Логика стрика (огонька)
            # Проверяем, была ли запись вчера
            last_log = await session.scalar(
                select(HabitLog)
                .where(HabitLog.habit_id == habit_id)
                .order_by(HabitLog.date_logged.desc())
            )
            
            is_streak = False
            if last_log:
                delta = datetime.now() - last_log.date_logged
                if delta.days == 0:
                    pass # Уже сегодня делал
                elif delta.days == 1:
                    habit.current_streak += 1
                    is_streak = True
                else:
                    habit.current_streak = 1 # Сброс стрика
            else:
                habit.current_streak = 1 # Первая запись

            if habit.current_streak > habit.longest_streak:
                habit.longest_streak = habit.current_streak
            
            habit.total_minutes += minutes
            session.add(HabitLog(habit_id=habit_id, minutes_spent=minutes))
            await session.commit()
            return habit.current_streak
        return 0

# Для статистики
async def get_habit_logs(habit_id):
    async with async_session() as session:
        result = await session.execute(select(HabitLog).where(HabitLog.habit_id == habit_id))
        return result.scalars().all()