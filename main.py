from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio

API_TOKEN = "7936831978:AAHRX2viqIzDhG3IvlvlZjUzD0rUHCub_3o"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def on_start(message: types.Message):
    await message.reply("Welcome to Reminder Bot!"
                        " Use /add <text> at <time> to set a reminder")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__"
    asyncio.run(main())