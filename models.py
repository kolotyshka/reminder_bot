import json
from aiogram import Bot
from datetime import datetime

class Task:
    def __init__(self, text, time, chat_id=None, separator="at", date=None):
        self.text = text
        self.time = time
        self.chat_id = chat_id
        self.separator = separator
        self.date = date

    def to_dict(self):
        """Преобразует задачу в словарь для JSON."""
        return {
            "text": self.text,
            "time": self.time,
            "chat_id": self.chat_id,
            "separator": self.separator,
            "date": self.date
        }

class TaskManager:
    def __init__(self):
        self.tasks = []

    async def send_task(self, task, bot: Bot):
        """Отправляет уведомление о задаче."""
        await bot.send_message(chat_id=task.chat_id, text=f"Reminder: {task.text}")

    def add_task(self, task):
        """Добавляет задачу в список."""
        self.tasks.append(task)

class Storage:
    def __init__(self):
        self.db = "reminders.json"

    def save_task(self, task):
        """Сохраняет задачу в JSON-файл."""
        data = []
        try:
            with open(self.db, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            pass
        data.append(task.to_dict())
        with open(self.db, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load_tasks(self):
        """Загружает задачи из JSON-файла."""
        try:
            with open(self.db, 'r', encoding='utf-8') as f:
                return [Task(
                    d["text"],
                    d["time"],
                    d.get("chat_id"),
                    d.get("separator", "at"),
                    d.get("date")
                ) for d in json.load(f)]
        except FileNotFoundError:
            return []