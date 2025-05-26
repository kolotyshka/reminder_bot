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
    await message.reply("Welcome to Reminder Bot! Use /add <text> at <time> [date] or /add <text> в <time> [date]")


@dp.message(Command("add"))
@log_command
async def on_add(message: types.Message):
    """Добавляет новую задачу с текстом, временем и датой."""
    try:
        raw_text = message.text
        with open("bot.log", "a", encoding="utf-8") as f:
            f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Raw input: {raw_text}\n")
        text = raw_text.encode('utf-8').decode('utf-8')

        # Проверяем разделитель
        separator = None
        separator_text = None
        if " at " in text:
            separator = " at "
            separator_text = "at"
        elif " в " in text:
            separator = " в "
            separator_text = "в"
        if not separator:
            await message.reply("Use: /add <text> at <time> [date] or /add <text> в <time> [date]")
            return

        # Разделяем на части
        parts = text.split(separator, 1)
        if len(parts) != 2:
            await message.reply("Use: /add <text> at <time> [date] or /add <text> в <time> [date]")
            return
        command, time_date = parts
        task_text = command.replace("/add", "").strip()
        if not task_text:
            await message.reply("Please provide reminder text")
            return

        # Парсим время и дату
        time_date = time_date.strip()
        time_str = time_date
        date_str = None
        if " " in time_date:
            time_str, date_str = time_date.split(" ", 1)
            date_str = date_str.strip()

        try:
            datetime.strptime(time_str, "%H:%M")
        except ValueError:
            await message.reply("Invalid time format! Use HH:MM (e.g., 14:30)")
            return

        if date_str:
            try:
                task_date = datetime.strptime(date_str, "%d.%m.%Y").strftime("%d.%m.%Y")
            except ValueError:
                await message.reply("Invalid date format! Use DD.MM.YYYY (e.g., 27.05.2025)")
                return
        else:
            task_date = datetime.now().strftime("%d.%m.%Y")

        # Проверяем, что дата/время в будущем
        task_datetime = datetime.strptime(f"{task_date} {time_str}", "%d.%m.%Y %H:%M")
        now = datetime.now().replace(second=0, microsecond=0)
        if task_datetime < now:
            with open("bot.log", "a", encoding="utf-8") as f:
                f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Rejected: {task_datetime} is before {now}\n")
            await message.reply("Cannot set reminder in the past!")
            return

        task = Task(task_text, time_str, message.chat.id, separator_text, task_date)
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
    response = "\n".join(
        f"{i + 1}. {t.text} {t.separator} {t.time} {t.date or ''}".strip()
        for i, t in enumerate(tasks)
    )
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
        current_datetime = datetime.now()
        current_date = current_datetime.strftime("%d.%m.%Y")
        current_time = current_datetime.strftime("%H:%M")
        tasks_to_remove = []
        for task in task_manager.tasks:
            task_date = task.date or current_date
            if task_date == current_date and task.time == current_time:
                await task_manager.send_task(task, bot)
                tasks_to_remove.append(task)
                with open("bot.log", "a", encoding="utf-8") as f:
                    f.write(
                        f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Sent reminder: {task.text} at {task.time} {task_date}\n")
        for task in tasks_to_remove:
            task_manager.tasks.remove(task)
        await asyncio.sleep(60)


async def main():
    """Запускает таймер и бота."""
    asyncio.create_task(check_tasks())
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())