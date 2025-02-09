from src.application.services.message_printer import MessagePrinter


class DisplayMessage:
  @staticmethod
  def backup_aborted() -> None:
    MessagePrinter.print_backup_aborted("Sauvegarde annulée par l'utilisateur...")


  @staticmethod
  def error(message: str) -> None:
    MessagePrinter.print_error(message)


  @staticmethod
  def exception(message: str) -> None:
    MessagePrinter.print_exception(message)


  @staticmethod
  def goodbye() -> None:
    MessagePrinter.print_message("👋 Programme terminé.")


  @staticmethod
  def info(message: str) -> None:
    MessagePrinter.print_info(message)


  @staticmethod
  def leave() -> None:
    MessagePrinter.print_message("👋 Interruption par l'utilisateur. Programme terminé.")


  @staticmethod
  def message(message: str) -> None:
    MessagePrinter.print_message(message)


  @staticmethod
  def saved_file_folder(message: str) -> None:
    MessagePrinter.print_saved_file_folder(message)


  @staticmethod
  def success(message: str) -> None:
    MessagePrinter.print_success(message)


  @staticmethod
  def warning(message: str) -> None:
    MessagePrinter.print_warning(message)


  @staticmethod
  def welcome() -> None:
    MessagePrinter.print_message("Bienvenue dans OpenScraper 🎣")
