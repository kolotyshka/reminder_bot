import json
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
for task in storage.load_tasks():
    task_manager.add_task(task)

@dp.message(Command("start"))
@log_command
async def on_start(message: types.Message):
    """Отправляет приветственное сообщение."""
    await message.reply("Welcome to Reminder Bot! Use /add <text> at <time> or /add <text> в <time>")

@dp.message(Command("add"))
@log_command
async def on_add(message: types.Message):
    """Добавляет новую задачу с текстом и временем."""
    try:
        # Декодируем текст
        raw_text = message.text
        with open("bot.log", "a", encoding="utf-8") as f:
            f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Raw input: {raw_text}\n")
        text = raw_text.encode('utf-8').decode('utf-8')
        # Проверяем оба разделителя
        separator = None
        separator_text = None
        if " at " in text:
            separator = " at "
            separator_text = "at"
        elif " в " in text:
            separator = " в "
            separator_text = "в"
        if not separator:
            await message.reply("Use: /add <text> at <time> or /add <text> в <time>")
            return
        parts = text.split(separator, 1)
        if len(parts) != 2:
            await message.reply("Use: /add <text> at <time> or /add <text> в <time>")
            return
        command, time = parts
        task_text = command.replace("/add", "").strip()
        if not task_text:
            await message.reply("Please provide reminder text")
            return
        try:
            datetime.strptime(time.strip(), "%H:%M")
        except ValueError:
            await message.reply("Invalid time format! Use HH:MM (e.g., 14:30)")
            return
        task = Task(task_text, time, message.chat.id, separator_text)
        task_manager.add_task(task)
        storage.save_task(task)
        await message.reply("Reminder set!")
    except Exception as e:
        await message.reply("Error adding reminder")
        with open("bot.log", "a", encoding="utf-8") as f:
            f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Error in on_add: {e}\n")

@dp.message(Command("list"))
@log_command
async def on_list(message: types.Message):
    """Показывает список всех задач."""
    tasks = storage.load_tasks()
    if not tasks:
        await message.reply("No reminders set.")
        return
    response = "\n".join(f"{i+1}. {t.text} {t.separator} {t.time}" for i, t in enumerate(tasks))
    await message.reply(f"Reminders:\n{response}")

@dp.message(Command("delete"))
@log_command
async def on_delete(message: types.Message):
    """Удаляет задачу по индексу."""
    try:
        index = int(message.text.split()[1]) - 1
        tasks = storage.load_tasks()
        if 0 <= index < len(tasks):
            tasks.pop(index)
            with open(storage.db, 'w', encoding="utf-8") as f:
                json.dump([t.to_dict() for t in tasks], f, ensure_ascii=False, indent=2)
            task_manager.tasks = tasks
            await message.reply("Reminder deleted!")
        else:
            await message.reply("Invalid index!")
    except (IndexError, ValueError):
        await message.reply("Use: /delete <index>")

async def check_tasks():
    """Проверяет задачи каждую минуту и отправляет уведомления."""
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
    """Запускает таймер и бота."""
    asyncio.create_task(check_tasks())
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())