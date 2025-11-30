import os
from datetime import datetime
from .Queue import Queue
from .Notification import Notification

class NotificationsSystem:
    def __init__(self, file_path):
        self.file_path = file_path
        self.noti_queue = Queue()
        self.load_notifications()

    def add_notification(self, title, description):
        date = datetime.now().strftime("%Y-%m-%d")
        n = Notification(date, title, description)
        self.noti_queue.enqueue(n)
        self.save_notifications()

    def save_notifications(self):
        with open(self.file_path, "w", encoding="utf-8") as f:
            for n in self.noti_queue.to_list():
                f.write(f"{n.date};{n.title};{n.description}\n")

    def load_notifications(self):
        if not os.path.exists(self.file_path):
            open(self.file_path, "w").close()
            return
        
        with open(self.file_path, "r", encoding="utf-8") as f:
            for line in f:
                date, title, desc = line.strip().split(";")
                self.noti_queue.enqueue(Notification(date, title, desc))

    def get_notifications(self):
        return self.noti_queue.to_list()
