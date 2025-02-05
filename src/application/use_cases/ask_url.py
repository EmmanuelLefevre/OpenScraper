from src.application.services.message_printer import MessagePrinter

class AskUrl:
  @staticmethod
  def execute() -> str:
    return MessagePrinter.ask_user_input("🏁 Saisir une URL")
