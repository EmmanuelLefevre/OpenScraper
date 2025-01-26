from app.functions.welcome_message import WelcomeMessage

class DisplayWelcome:
  @staticmethod
  def execute():
    WelcomeMessage.print_welcome_message()
