from src.application.services.message_printer import MessagePrinter


class DisplayException:
  @staticmethod
  def execute(message: str) -> None:
    MessagePrinter.print_exception(message)
