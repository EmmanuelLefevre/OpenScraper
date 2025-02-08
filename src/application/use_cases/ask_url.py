from src.application.services.message_printer import MessagePrinter


class AskUrl:
  @staticmethod
  def execute() -> str:
    url = MessagePrinter.ask_user_input("🏁 Saisir une URL")
    return url.strip()
