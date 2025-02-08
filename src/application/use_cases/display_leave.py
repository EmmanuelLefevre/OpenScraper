from src.application.services.message_printer import MessagePrinter

class DisplayLeave:
  @staticmethod
  def execute() -> None:
    MessagePrinter.print_message("👋 Interruption par l'utilisateur. Programme terminé.")
