class Payment:
    def __init__(self, payment_id, user_id, amount):
        self.payment_id = payment_id
        self.user_id = user_id
        self.amount = amount

    def process_payment(self):
        print(f"Payment of R{self.amount} by user {self.user_id} processed.")
