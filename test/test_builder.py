import unittest
from creational_patterns.builder import PizzaBuilder

class TestBuilderPattern(unittest.TestCase):
    def test_build_pizza(self):
        builder = PizzaBuilder()
        pizza = builder.add_cheese().add_toppings(["mushrooms", "olives"]).build()
        self.assertIn("mushrooms", pizza.toppings)
        self.assertTrue(pizza.cheese)
