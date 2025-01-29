from colorama import Fore, Style

class MessagePrinter:
  @staticmethod
  def print_success(message: str):
    print(f"{Style.BRIGHT}{Fore.GREEN}✅ {message}{Style.RESET_ALL}")

  @staticmethod
  def print_info(message: str):
    print(f"{Style.BRIGHT}{Fore.BLUE}ℹ {message}{Style.RESET_ALL}")

  @staticmethod
  def print_warning(message: str):
    print(f"{Style.BRIGHT}{Fore.MAGENTA}⚠️ {message}{Style.RESET_ALL}")

  @staticmethod
  def print_error(message: str):
    print(f"{Style.BRIGHT}{Fore.RED}💥 {message}{Style.RESET_ALL}")

  @staticmethod
  def ask_user_input(message: str):
    print(f"💬 {message} ('fin' pour quitter) : ", end="")

  @staticmethod
  def ask_user_confirmation(message: str, default: bool = True):
    options = "(O/n)" if default else "(o/N)"
    print(f"💬 {message} {options} : ", end="")

  @staticmethod
  def print_welcome_message():
    print(f"{Style.BRIGHT}{Fore.BLUE}Bienvenue dans OpenScraper 🎣{Style.RESET_ALL}")

  @staticmethod
  def print_goodbye_message():
    print(f"{Style.BRIGHT}{Fore.BLUE}👋 Programme terminé.{Style.RESET_ALL}")