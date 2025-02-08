from src.application.exceptions.user_exit_exception import UserExitException
from src.application.services.message_printer import MessagePrinter
from src.application.use_cases.display_warning import DisplayWarning


class UserInputHandler:
  @staticmethod
  def ask_input(message: str, allow_empty: bool = False) -> str:

    while True:
      user_input = MessagePrinter.ask_user_input(message).strip()

      if user_input.lower() == "fin":
        raise UserExitException

      if user_input or allow_empty:
        return user_input

      DisplayWarning.execute("La saisie ne peut être vide! Essayer à nouveau...")
