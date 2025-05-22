class Reminder:
    def __init__(self, text, time):
        self.text = text
        self.time = time

    def to_dict(self):
        return {"text": self.text, "time": self.time}

class Bot:
    def __init__(self):
        self.reminders = []

    async def send_reminder(self, reminder):
        pass

    def add_reminder(self, reminder):
        self.reminders.append(reminder)

class Storage:
    def __init__(self):
        self.db = None

    def save_reminder(self, reminder):
        pass

    def load_reminders(self):
        return []