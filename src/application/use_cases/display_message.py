from src.application.services.message_printer import MessagePrinter


class DisplaySuccess:
  @staticmethod
  def execute(message: str) -> None:
    MessagePrinter.print_success(message)
