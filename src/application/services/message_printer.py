from colorama import Fore, Style


class MessagePrinter:
  @staticmethod
  def ask_user_confirmation(message: str, default: bool = True) -> str:
    options = "(O/n)" if default else "(o/N)"
    return input (f"💬 {message} {options} : \n")


  @staticmethod
  def ask_user_input(message: str) -> str:
    return input(f"{message} ('fin' pour quitter) : \n")


  @staticmethod
  def print_backup_aborted(message: str) -> None:
    print(f"{Style.BRIGHT}{Fore.RED}❌ {message}{Style.RESET_ALL}")


  @staticmethod
  def print_error(message: str) -> None:
    print(f"{Style.BRIGHT}{Fore.RED}💥 {message}{Style.RESET_ALL}")


  @staticmethod
  def print_exception(message: str) -> None:
    print(f"{Style.NORMAL}{Fore.RED}💣 {message}{Style.RESET_ALL}")


  @staticmethod
  def print_info(message: str) -> None:
    print(f"{Style.BRIGHT}{Fore.CYAN}ℹ  {message}{Style.RESET_ALL}")


  @staticmethod
  def print_message(message: str) -> None:
    print(f"{Style.NORMAL}{Fore.BLUE}{message}{Style.RESET_ALL}")


  @staticmethod
  def print_saved_file_folder(message: str) -> None:
    print(f"{Style.BRIGHT}{Fore.GREEN}📄 {message}{Style.RESET_ALL}")


  @staticmethod
  def print_success(message: str) -> None:
    print(f"{Style.BRIGHT}{Fore.GREEN}✅ {message}{Style.RESET_ALL}")


  @staticmethod
  def print_warning(message: str) -> None:
    print(f"{Style.BRIGHT}{Fore.MAGENTA}⚠️ {message}{Style.RESET_ALL}")
