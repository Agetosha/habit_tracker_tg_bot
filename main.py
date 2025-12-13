import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from database.models import async_main
from handlers import start, creation, tracking, statistics

async def main():
    # Создание таблиц БД при запуске
    await async_main()
    
    # Настройка бота
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    
    # Подключение роутеров (хендлеров)
    dp.include_router(start.router)
    dp.include_router(creation.router)
    dp.include_router(tracking.router)
    dp.include_router(statistics.router)
    
    print("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")