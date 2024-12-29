# Here your solution
from abc import ABC, abstractmethod 
class paymethod(ABC):
    @abstractmethod
    def calculate_fee(self, amount:float):
        pass

class creditcard(paymethod):
    def calculate_fee(self, amount:float):
        return amount * 0.03
    
class paypalmethod(paymethod):
    def calculate_fee(self,amount:float):
        return amount *0.05

class banktransfer (paymethod):
    def calculate_fee(self,amount:float):
        return amount*2.50
    
class fee_calculator:
    def __init__(self,payment_method:paymethod):
        self.payment_method = payment_method
    def calculate_fee(self,amount:float):
        return self.payment_method.calculate_fee(amount)