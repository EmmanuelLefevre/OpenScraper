from src.application.services.message_printer import MessagePrinter


class DisplayWelcome:
  @staticmethod
  def execute() -> None:
    MessagePrinter.print_message("Bienvenue dans OpenScraper 🎣")
