class UserInput:
  @staticmethod
  def ask_user_confirmation(message: str, default: bool = True) -> str:
    options = "(O/n)" if default else "(o/N)"
    return input(f"💬 {message} {options} : \n")

  @staticmethod
  def ask_user_input(message: str) -> str:
    return input(f"{message} ('fin' pour quitter) : \n")
