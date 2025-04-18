import unittest
from creational_patterns.factory_method.concrete_classes import CreditCardProcessor, PayPalProcessor

class TestFactoryMethod(unittest.TestCase):
    def test_credit_card_payment(self):
        processor = CreditCardProcessor()
        self.assertEqual(processor.process_payment(100), "Processed 100 with Credit Card")

    def test_paypal_payment(self):
        processor = PayPalProcessor()
        self.assertEqual(processor.process_payment(200), "Processed 200 with PayPal")
