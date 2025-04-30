from src.adapters.display_message import ConsoleMessageDisplayAdapter

class DisplayMessage:
  _adapter = ConsoleMessageDisplayAdapter()

  @staticmethod
  def backup_aborted() -> None:
    DisplayMessage._adapter.display("Sauvegarde annulée par l'utilisateur...", "backup_aborted")

  @staticmethod
  def error(message: str) -> None:
    DisplayMessage._adapter.display(message, "error")

  @staticmethod
  def exception(message: str) -> None:
    DisplayMessage._adapter.display(message, "exception")

  @staticmethod
  def goodbye() -> None:
    DisplayMessage._adapter.display("👋 Programme terminé.", "message")

  @staticmethod
  def info(message: str) -> None:
    DisplayMessage._adapter.display(message, "info")

  @staticmethod
  def leave() -> None:
    DisplayMessage._adapter.display("👋 Interruption par l'utilisateur. Programme terminé.", "message")

  @staticmethod
  def message(message: str) -> None:
    DisplayMessage._adapter.display(message, "message")

  @staticmethod
  def saved_file_folder(message: str) -> None:
    DisplayMessage._adapter.display(message, "saved_file")

  @staticmethod
  def success(message: str) -> None:
    DisplayMessage._adapter.display(message, "success")

  @staticmethod
  def warning(message: str) -> None:
    DisplayMessage._adapter.display(message, "warning")

  @staticmethod
  def welcome() -> None:
    DisplayMessage._adapter.display("Bienvenue dans OpenScraper 🎣", "message")
