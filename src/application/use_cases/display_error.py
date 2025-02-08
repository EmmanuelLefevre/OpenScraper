from src.application.services.message_printer import MessagePrinter


class DisplayError:
  @staticmethod
  def execute(message: str) -> None:
    MessagePrinter.print_error(message)
