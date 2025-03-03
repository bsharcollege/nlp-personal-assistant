from datetime import datetime

class CalendarManager:
    def __init__(self):
        self.events = []
        self.reminders = []

    def add_event(self, event):
        self.events.append(event)

    def remove_event(self, event):
        if event in self.events:
            self.events.remove(event)

    def list_events(self):
        return self.events

    def create_reminder(self, subject, start_time):
        reminder = {
            "subject": subject,
            "start_time": start_time
        }
        self.reminders.append(reminder)
        return reminder

    def get_reminders(self):
        return self.reminders