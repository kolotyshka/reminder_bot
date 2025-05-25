import json
from aiogram import Bot
from datetime import datetime

class Task:
    def __init__(self, text, time, chat_id=None, separator="at"):
        self.text = text
        self.time = time
        self.chat_id = chat_id
        self.separator = separator

    def to_dict(self):
        """Преобразует задачу в словарь для JSON."""
        return {
            "text": self.text,
            "time": self.time,
            "chat_id": self.chat_id,
            "separator": self.separator
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
        except (FileNotFoundError, json.JSONDecodeError) as e:
            with open("bot.log", "a", encoding="utf-8") as f:
                f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Load error: {e}\n")
        data.append(task.to_dict())
        try:
            with open(self.db, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            with open("bot.log", "a", encoding="utf-8") as f:
                f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Save error: {e}\n")

    def load_tasks(self):
        """Загружает задачи из JSON-файла."""
        try:
            with open(self.db, 'r', encoding='utf-8') as f:
                return [Task(
                    d["text"],
                    d["time"],
                    d.get("chat_id"),
                    d.get("separator", "at")  # По умолчанию "at" для старых задач
                ) for d in json.load(f)]
        except (FileNotFoundError, json.JSONDecodeError) as e:
            with open("bot.log", "a", encoding="utf-8") as f:
                f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Load error: {e}\n")
            return []