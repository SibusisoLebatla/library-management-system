class User:
    def __init__(self, user_id, name, email, password):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.borrowed_books = []

    def register(self):
        print(f"{self.name} registered successfully.")

    def login(self):
        print(f"{self.name} logged in.")

    def delete(self):
        print(f"{self.name} account deleted.")

