# Here your solution
from abc import ABC, abstractmethod
import datetime

class tranasactionlongger(ABC):
    @abstractmethod
    def log_transaction(self, message:str):
            pass

class notificationservice(ABC):
    @abstractmethod
    def send_notification(self, message:str):
        pass

class filetransactionlogger(tranasactionlongger):
    def __init__(self, log_file:str):
        self.log_file = log_file

    def log(self,message:str):
        with open(self.log_file, "a") as log_file:
            log_file.write(f"{datetime.datetime.now()}: {message}\n")

class emailnotificationservice(notificationservice):
    def send_notification(self, message:str):
        print(f"sending email notificacion: {message}")

class bankaccount:
    def __init__(self, account_number:str, transaction_logger: tranasactionlongger, notification_service: notificationservice, balance: float = 0.0):
        self.account_number = account_number
        self.balance = balance
        self.transaction_logger = transaction_logger
        self.notification_service = notification_service
        
def deposit(self, amount :float):
    if amount <= 0:
        raise ValueError("deposit amount must be positive.")
    self.balance += amount

    self.transaction_logger.log_transaction(f"Deposited {amount} into {self.account_number}")
    self.notification_service.send_notification(f"{amount} deposited into account {self.account_number}")

def withdraw(self, amount: float):
    if amount <= 0:
        raise ValueError("withdrawal amount must be positive.")
    if amount > self.balance:
        raise ValueError("Insufficient funds.")

    self.balance -= amount

    self.transaction_logger.log_transaction(f"Withdrew {amount} from {self.account_number}")
    self.notification_service.send_notification(f"{amount} withdrawn from account {self.account_number}")   

def generate_statement(self):
    statement= f"Statement for Account: {self.account_number}\nBalance: {self.balance}\n"
    print(statement)

    self.transaction_logger.log_transaction(f"Generated statement for {self.account_number}")
    self.notification_service.send_notification(f"statement for account {self.account_number} has been sent via email")