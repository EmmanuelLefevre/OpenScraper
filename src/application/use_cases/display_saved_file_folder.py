from src.application.services.message_printer import MessagePrinter


class DisplaySavedFileFolder:
  @staticmethod
  def execute(message: str) -> None:
    MessagePrinter.print_saved_file_folder(message)
