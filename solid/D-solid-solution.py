# Here your solution
from abc import ABC, abstractmethod

class paymentservice(ABC):
    @abstractmethod
    def pay(self, amount:float):
        pass
        

class paypalservice(paymentservice):
    def pay (self, amount:float):
        print(f"paying {amount} using paypal")
        

class creditcardservice(paymentservice):
    def pay(self, amount:float):
        print(f"paying{amount} using creditcard")

class debitcardservice(paymentservice):
    def pay(self, amount:float):
        print(f"paying{amount} using debitcard")

class yapeservice(paymentservice):
    def pay(self, amount:float):
        print(f"paying{amount} using yape")


class paymentprocessor:
    def __init__(self):
        self.payment_service = paymentservice
    def process_payment(self, amount:float):
        self.payment_service.pay(amount)