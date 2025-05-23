
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio

from decorators import log_command
from models import Reminder

API_TOKEN = "7936831978:AAHRX2viqIzDhG3IvlvlZjUzD0rUHCub_3o"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def on_start(message: types.Message):
    await message.reply("Welcome to Reminder Bot!"
                        " Use /add <text> at <time> to set a reminder")

@dp.message(Command("add"))
@log_command
async def on_add(message: types.Message):
    parts = message.text.split(" at ", 1)
    if len (parts) != 2:
        await message.reply("Use: /add <text> at <time>")
        return
    text, time = parts
    reminder = Reminder(text, time)
    Bot().add_reminder(reminder)
    await message.reply
    await message.reply("Reminder set!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())