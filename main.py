from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio
from datetime import datetime
from decorators import log_command
from models import Reminder, Bot as ReminderBot, Storage

API_TOKEN = "7936831978:AAHRX2viqIzDhG3IvlvlZjUzD0rUHCub_3o"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
bot_instance = ReminderBot()
storage = Storage()

for reminder in storage.load_reminders():
    bot_instance.add_reminder(reminder)

@dp.message(Command("start"))
async def on_start(message: types.Message):
    await message.reply("Welcome to Reminder Bot!"
                        " Use /add <text> at <time> to set a reminder")

@dp.message(Command("add"))
@log_command
async def on_add(message: types.Message):
    parts = message.text.split(" at ", 1)
    if len(parts) != 2:
        await message.reply("Use: /add <text> at <time>")
        return
    command, time = parts
    text = command.replace("/add", "").strip()
    if not text:
        await message.reply("Please provide reminder text")
        return
    try:
        datetime.strptime(time.strip(), "%H:%M")
    except ValueError:
        await message.reply("Invalid time format! Use HH:MM (e.g. 14:30)")
        return
    reminder = Reminder(text, time, message.chat.id)
    bot_instance.add_reminder(reminder)
    storage.save_reminder(reminder)
    await message.reply("Reminder set!")

async def check_reminders():
    while True:
        current_time = datetime.now().strftime("%H:%M")
        reminders_to_remove = []
        for reminder in bot_instance.reminders:
            if reminder.time == current_time:
                await bot.send_message(chat_id=reminder.chat_id,
                                       text = f"Reminder: {reminder.text}")
                reminders_to_remove.append(reminder)
        for reminder in reminders_to_remove:
            bot_instance.reminders.remove(reminder)
        await  asyncio.sleep(60)

async def main():
    asyncio.create_task(check_reminders())
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())