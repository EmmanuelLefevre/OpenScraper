class PrintMessage:
  @staticmethod
  def print_info(message: str):
    print(f"[INFO]: {message}")

  @staticmethod
  def print_warning(message: str):
    print(f"[WARNING]: {message}")

  @staticmethod
  def print_error(message: str):
    print(f"[ERROR]: {message}")
