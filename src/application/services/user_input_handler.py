from src.application.exceptions.user_exit_exception import UserExitException
from src.application.services.message_printer import MessagePrinter


class UserInputHandler:
  @staticmethod
  def ask_input(message: str) -> str:
    user_input = MessagePrinter.ask_user_input(message)

    if user_input.strip().lower() == "fin":
      raise UserExitException
    return user_input.strip()
