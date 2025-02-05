from src.application.services.message_printer import MessagePrinter

class DisplayGoodbye:
  @staticmethod
  def execute():
    MessagePrinter.print_message("👋 Programme terminé.")
