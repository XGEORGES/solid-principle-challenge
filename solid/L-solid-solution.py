# Here your solution
from abc import ABC, abstractmethod
class payprocessor(ABC):
    @abstractmethod
    def pay(self, amount:float):
        pass

class refundprocessor(ABC):
    @abstractmethod
    def refund(self, amount:float):
        pass

class paymethod:
    def __init__(self,balance:float):
        self.balance = balance

class Genericpay(paymethod, payprocessor, refundprocessor):
    def pay(self, amount: float) -> None:
        if amount>self.balance:
            raise ValueError("Not enough balance.")
        self.balance -= amount
        print(f"[Genericpayment] Paid {amount}. New balance: {self.balance}")

    def refund(self,amount:float)-> None:
        self.balance +=amount
        print(f"[Genericpayment] Refunded {amount}. New balance: {self.balance}")

class NonRefundableGiftCard(paymethod,payprocessor):
    def pay(self, amount: float) -> None:
        if amount > self.balance:
            raise ValueError("Not enough balance.")
        self.balance -= amount
        print(f"[NonRefundableGiftCard] Paid {amount}. New balance: {self.balance}")