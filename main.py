# стандартные модули Python
import asyncio  # для асинхронного выполнения
import logging  # для записи логов работы бота

# ядро телеграм-бота
from aiogram import Bot, Dispatcher  # Bot - сам бот, Dispatcher - маршрутизатор сообщений

# конфигурация
from config import BOT_TOKEN  # секретный токен для подключения к API Telegram

# инициализация БД
from database.models import async_main  # функция создания таблиц при запуске

# все обработчики команд и сообщений
from handlers import start, creation, tracking, statistics

async def main():
    # создаем таблицы в базе данных при запуске
    await async_main()
    
    # настраиваем бота
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    
    # подключаем роутеры (обработчики сообщений)
    dp.include_router(start.router)
    dp.include_router(creation.router)
    dp.include_router(tracking.router)
    dp.include_router(statistics.router)
    
    print("Бот запущен!")
    await dp.start_polling(bot)  # запускаем опрос серверов телеграма

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")