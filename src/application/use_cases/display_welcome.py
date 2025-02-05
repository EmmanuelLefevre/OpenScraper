from src.application.services.message_printer import MessagePrinter

class DisplayWelcome:
  @staticmethod
  def execute():
    MessagePrinter.print_message("Bienvenue dans OpenScraper 🎣")
