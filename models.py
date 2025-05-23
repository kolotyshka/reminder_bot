import json

class Reminder:
    def __init__(self, text, time, chat_id):
        self.text = text
        self.time = time
        self.chat_id = chat_id

    def to_dict(self):
        return {"text": self.text, "time": self.time, "chat_id": self.chat_id}

class Bot:
    def __init__(self):
        self.reminders = []

    async def send_reminder(self, reminder):
        pass

    def add_reminder(self, reminder):
        self.reminders.append(reminder)

class Storage:
    def __init__(self):
        self.db = "reminders.json"

    def save_reminder(self, reminder):
        data = []
        try:
            with open(self.db, 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            pass
        data.append(reminder.to_dict())
        with open(self.db, 'w') as f:
            json.dump(data, f)

    def load_reminders(self):
        try:
            with open(self.db, 'r') as f:
                return [Reminder(d["text"], d["time"], d["chat_id"]) for d in json.load(f)]
        except FileNotFoundError:
            return []