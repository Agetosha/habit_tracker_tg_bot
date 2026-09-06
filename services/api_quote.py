# библиотека для асинхронных HTTP-запросов
import aiohttp

# модуль для логирования (записи информации о работе программы)
import logging

async def get_motivation_quote():
    # получаем мотивационную цитату из внешнего api
    url = "https://zenquotes.io/api/random"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    q = data[0]['q']  # текст цитаты
                    a = data[0]['a']  # автор
                    return f"💡 <b>Мудрость дня:</b>\n\n_«{q}»_\n— {a}"
                else:
                    logging.error(f"API Error: {response.status}")
    except Exception as e:
        logging.error(f"API Connection Error: {e}")
    
    # заглушка на случай недоступности api
    return "💡 <b>Мудрость дня:</b>\n\n_«Дисциплина — это решение делать то, чего очень не хочется делать, чтобы достичь того, чего очень хочется достичь.»_"