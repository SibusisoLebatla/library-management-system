from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Credit Card payment of {amount} processed"

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"PayPal payment of {amount} processed"
