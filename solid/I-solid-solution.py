# Here your solution
from abc import ABC, abstractmethod

class Paymentprocessor(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass

class regfundprocessor(ABC):
    @abstractmethod
    def refund(self, amount: float) -> None:
        pass
class handledispute(ABC):
    @abstractmethod
    def handle_dispute(self, dispute_id: str) -> None:
        pass

class BasicGiftCard(Paymentprocessor):
    def pay(self, amount: float) -> None:
        print(f"Gift card used to pay {amount}.")