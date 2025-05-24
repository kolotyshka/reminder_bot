from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio
from datetime import datetime
from decorators import log_command
from models import Task, TaskManager, Storage
from config import API_TOKEN

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
task_manager = TaskManager()
storage = Storage()

# Загружаем задачи при старте
# Load tasks at startup
for task in storage.load_tasks():
    task_manager.add_task(task)

@dp.message(Command("start"))
@log_command
async def on_start(message: types.Message):
    """Отправляет приветственное сообщение.
    Sends a welcome message."""
    await message.reply("Welcome to Reminder Bot! Use /add <text> at <time> to set a reminder")

@dp.message(Command("add"))
@log_command
async def on_add(message: types.Message):
    """Добавляет новую задачу с текстом и временем.
    Adds a new task with text and time."""
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
        await message.reply("Invalid time format! Use HH:MM (e.g., 14:30)")
        return
    task = Task(text, time, message.chat.id)
    task_manager.add_task(task)
    storage.save_task(task)
    await message.reply("Reminder set!")

@dp.message(Command("list"))
@log_command
async def on_list(message: types.Message):
    """Показывает список всех задач.
    Shows a list of all tasks."""
    tasks = storage.load_tasks()
    if not tasks:
        await message.reply("No reminders set.")
        return
    response = "\n".join(f"{t.text} at {t.time}" for t in tasks)
    await message.reply(f"Reminders:\n{response}")

async def check_tasks():
    """Проверяет задачи каждую минуту и отправляет уведомления.
    Checks tasks every minute and sends notifications."""
    while True:
        current_time = datetime.now().strftime("%H:%M")
        tasks_to_remove = []
        for task in task_manager.tasks:
            if task.time == current_time:
                await task_manager.send_task(task, bot)
                tasks_to_remove.append(task)
        for task in tasks_to_remove:
            task_manager.tasks.remove(task)
        await asyncio.sleep(60)

async def main():
    """Запускает таймер и бота.
    Starts the timer and the bot."""
    asyncio.create_task(check_tasks())
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())