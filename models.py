import json

class Task:
    def __init__(self, text, time, chat_id=None):
        self.text = text
        self.time = time
        self.chat_id = chat_id

    def to_dict(self):
        return {"text": self.text, "time": self.time, "chat_id": self.chat_id}

class TaskManager:
    def __init__(self):
        self.tasks = []

    async def send_task(self, task):
        pass

    def add_task(self, task):
        self.tasks.append(task)

class Storage:
    def __init__(self):
        self.db = "reminders.json"

    def save_task(self, task):
        data = []
        try:
            with open(self.db, 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            pass
        data.append(task.to_dict())
        with open(self.db, 'w') as f:
            json.dump(data, f)

    def load_tasks(self):
        try:
            with open(self.db, 'r') as f:
                return [Task(d["text"], d["time"], d.get("chat_id")) for d in json.load(f)]
        except FileNotFoundError:
            return []