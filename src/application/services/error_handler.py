import logging
import os
import traceback

from src.application.use_cases.display_error import DisplayError

class ErrorHandler:
  LOG_DIR = "logs"
  LOG_FILE = os.path.join(LOG_DIR, "app.log")


  @staticmethod
  def setup_logging():
    if not os.path.exists(ErrorHandler.LOG_DIR):
      os.makedirs(ErrorHandler.LOG_DIR)

    logger = logging.getLogger("app_logger")
    if logger.hasHandlers():
      return logger

    logger.setLevel(logging.ERROR)

    file_handler = logging.FileHandler(ErrorHandler.LOG_FILE)
    file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter("%(levelname)s - %(message)s"))

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

  logger = setup_logging.__func__()


  @staticmethod
  def handle(error: Exception | str, log: bool = True):
    message = str(error)

    if isinstance(error, Exception):
      message += f"\n{traceback.format_exc()}"

    if log:
      ErrorHandler.logger.error(message)
    DisplayError.execute(str(error))
