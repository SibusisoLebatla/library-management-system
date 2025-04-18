class Loan:
    def __init__(self, loan_id, due_date, book, user):
        self.loan_id = loan_id
        self.due_date = due_date
        self.book = book
        self.user = user

    def calculate_fine(self, return_date):
        delta = (return_date - self.due_date).days
        fine = 0
        if delta > 0:
            fine = delta * 2  # R2 per day fine
        return fine
