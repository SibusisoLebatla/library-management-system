class Book:
    def __init__(self, book_id, title, author, status="available"):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.status = status

    def check_out(self):
        if self.status == "available":
            self.status = "checked_out"
            print(f"{self.title} checked out.")
        else:
            print(f"{self.title} is already checked out.")

    def return_book(self):
        self.status = "available"
        print(f"{self.title} returned.")
