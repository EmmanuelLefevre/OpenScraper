from src.application.services.message_printer import MessagePrinter


class DisplayMessage:
  @staticmethod
  def execute(message: str) -> None:
    MessagePrinter.print_message(message)
