from src.application.services.user_input_handler import UserInputHandler


class AskUrl:
  @staticmethod
  def execute() -> str:
    return UserInputHandler.ask_input("🏁 Saisir une URL")
