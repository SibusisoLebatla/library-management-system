class Staff:
    def __init__(self, staff_id, name, role):
        self.staff_id = staff_id
        self.name = name
        self.role = role

    def manage_loans(self):
        print(f"Staff {self.name} managing loans.")
