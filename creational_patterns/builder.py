class Pizza:
    def __init__(self):
        self.cheese = False
        self.pepperoni = False
        self.veggies = []

    def __str__(self):
        return f"Pizza(cheese={self.cheese}, pepperoni={self.pepperoni}, veggies={self.veggies})"

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def add_cheese(self):
        self.pizza.cheese = True
        return self

    def add_pepperoni(self):
        self.pizza.pepperoni = True
        return self

    def add_veggies(self, veggies):
        self.pizza.veggies.extend(veggies)
        return self

    def build(self):
        return self.pizza
