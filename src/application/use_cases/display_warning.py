from src.application.services.message_printer import MessagePrinter


class DisplayWarning:
  @staticmethod
  def execute(message: str):
    MessagePrinter.print_warning(f"{message}")
