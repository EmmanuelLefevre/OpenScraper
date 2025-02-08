from src.application.services.message_printer import MessagePrinter


class DisplayGoodbye:
  @staticmethod
  def execute() -> None:
    MessagePrinter.print_message("👋 Programme terminé.")
