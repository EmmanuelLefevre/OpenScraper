from src.application.services.message_printer import MessagePrinter

class DisplayLeave:
  @staticmethod
  def execute():
    MessagePrinter.print_message("\n👋 Interruption par l'utilisateur. Programme terminé.")
