class Notification:
    def __init__(self, notification_id, user_id, message):
        self.notification_id = notification_id
        self.user_id = user_id
        self.message = message

    def send(self):
        print(f"Notification sent to user {self.user_id}: {self.message}")
