from abc import ABC, abstractmethod
from colorama import Fore, Style
from src.application.use_cases.user_input import UserInput

class Message(ABC):
    @abstractmethod
    def display(self) -> None:
        pass

class ErrorMessage(Message):
    def __init__(self, message: str):
        self.message = message
    def display(self) -> None:
        print(f"{Style.BRIGHT}{Fore.RED}💥 {self.message}{Style.RESET_ALL}")

class ExceptionMessage(Message):
    def __init__(self, message: str):
        self.message = message
    def display(self) -> None:
        print(f"{Style.NORMAL}{Fore.RED}💣 {self.message}{Style.RESET_ALL}")

class InfoMessage(Message):
    def __init__(self, message: str):
        self.message = message
    def display(self) -> None:
        print(f"{Style.BRIGHT}{Fore.CYAN}ℹ  {self.message}{Style.RESET_ALL}")

class SimpleMessage(Message):
    def __init__(self, message: str):
        self.message = message
    def display(self) -> None:
        print(f"{Style.NORMAL}{Fore.BLUE}{self.message}{Style.RESET_ALL}")

class SavedFileMessage(Message):
    def __init__(self, message: str):
        self.message = message
    def display(self) -> None:
        print(f"{Style.BRIGHT}{Fore.GREEN}📄 {self.message}{Style.RESET_ALL}")

class SuccessMessage(Message):
    def __init__(self, message: str):
        self.message = message
    def display(self) -> None:
        print(f"{Style.BRIGHT}{Fore.GREEN}✅ {self.message}{Style.RESET_ALL}")

class WarningMessage(Message):
    def __init__(self, message: str):
        self.message = message
    def display(self) -> None:
        print(f"{Style.BRIGHT}{Fore.MAGENTA}⚠️ {self.message}{Style.RESET_ALL}")

class BackupAbortedMessage(Message):
    def __init__(self, message: str):
        self.message = message
    def display(self) -> None:
        print(f"{Style.BRIGHT}{Fore.RED}❌ {self.message}{Style.RESET_ALL}")
        user_input = UserInput.ask_user_input("Votre message ici")
