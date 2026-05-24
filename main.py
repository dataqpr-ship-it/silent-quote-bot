import asyncio
import os
from telegram import Bot

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TOKEN)

def load_quotes():
    with open("quotes.txt", "r", encoding="utf-8") as f:
        return [q.strip() for q in f.read().split("\n\n") if q.strip()]

def get_last_index():
    try:
        with open("last_index.txt", "r") as f:
            return int(f.read().strip())
    except:
        return 0

def save_last_index(index):
    with open("last_index.txt", "w") as f:
        f.write(str(index))

async def send_quote():

    quotes = load_quotes()

    index = get_last_index()

    if index >= len(quotes):
        index = 0

    quote = quotes[index]

    message = quote

    await bot.send_message(
        chat_id=CHAT_ID,
        text=message
    )

    save_last_index(index + 1)

async def main():

    while True:

        try:
            await send_quote()
            print("Quote terkirim")
        except Exception as e:
            print(e)

        await asyncio.sleep(7200)

asyncio.run(main())
