import json
from aiogram import Bot

class Task:
    def __init__(self, text, time, chat_id=None):
        self.text = text
        self.time = time
        self.chat_id = chat_id

    def to_dict(self):
        """Преобразует задачу в словарь для JSON.
        Converts the task to a dictionary for JSON."""
        return {"text": self.text, "time": self.time, "chat_id": self.chat_id}

class TaskManager:
    def __init__(self):
        self.tasks = []

    async def send_task(self, task, bot: Bot):
        """Отправляет уведомление о задаче.
        Sends a task notification."""
        await bot.send_message(chat_id=task.chat_id, text=f"Reminder: {task.text}")

    def add_task(self, task):
        """Добавляет задачу в список.
        Adds a task to the list."""
        self.tasks.append(task)

class Storage:
    def __init__(self):
        self.db = "reminders.json"

    def save_task(self, task):
        """Сохраняет задачу в JSON-файл.
        Saves the task to a JSON file."""
        data = []
        try:
            with open(self.db, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            pass
        data.append(task.to_dict())
        with open(self.db, 'w', encoding='utf-8') as f:
            json.dump(data, f)

    def load_tasks(self):
        """Загружает задачи из JSON-файла.
        Loads tasks from a JSON file."""
        try:
            with open(self.db, 'r', encoding='utf-8') as f:
                return [Task(d["text"], d["time"], d.get("chat_id")) for d in json.load(f)]
        except FileNotFoundError:
            return []