from src.application.services.message_printer import MessagePrinter

class DisplayException:
  @staticmethod
  def execute(message: str):
    MessagePrinter.print_exception(message)
