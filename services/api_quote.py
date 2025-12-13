import aiohttp
import logging

async def get_motivation_quote():
    url = "https://zenquotes.io/api/random"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    q = data[0]['q']
                    a = data[0]['a']
                    return f"💡 <b>Мудрость дня:</b>\n\n_«{q}»_\n— {a}"
                else:
                    logging.error(f"API Error: {response.status}")
    except Exception as e:
        logging.error(f"API Connection Error: {e}")
    
    # Заглушка, если API сломалось
    return "💡 <b>Мудрость дня:</b>\n\n_«Дисциплина — это решение делать то, чего очень не хочется делать, чтобы достичь того, чего очень хочется достичь.»_"