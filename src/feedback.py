class Feedback:
    def __init__(self, feedback_id, user_id, content):
        self.feedback_id = feedback_id
        self.user_id = user_id
        self.content = content

    def submit(self):
        print(f"Feedback from user {self.user_id}: {self.content}")
