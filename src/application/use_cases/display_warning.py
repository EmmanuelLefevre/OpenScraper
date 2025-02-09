from src.application.services.message_printer import MessagePrinter


class DisplayWarning:
  @staticmethod
  def execute(message: str) -> None:
    MessagePrinter.print_warning(message)
