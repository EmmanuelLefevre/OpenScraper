from src.application.services.message_printer import MessagePrinter


class DisplayInfo:
  @staticmethod
  def execute(message: str) -> None:
    MessagePrinter.print_info(message)
