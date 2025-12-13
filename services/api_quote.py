import aiohttp

async def get_motivation_quote():
    url = "https://zenquotes.io/api/random"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                # Возвращаем цитату и автора
                return f"💡 <b>Мудрость дня:</b>\n\n_«{data[0]['q']}»_\n— {data[0]['a']}"
            return "Ты молодец! Продолжай в том же духе!"