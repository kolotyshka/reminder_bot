class Reminder:
    def __init__(self, text, time):
        self.text = text
        self.time = time

class Bot:
    def __init__(self):
        self.reminders = []

    async def send_reminder(self, reminder):
        pass

class Storage:
    def __init__(self):
        self.db = None

    def save_reminder(self, reminder):
        pass