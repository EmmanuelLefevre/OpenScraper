import logging
import os

from src.application.use_cases.display_error import DisplayError

class ErrorHandler:
  LOG_DIR = "logs"
  LOG_FILE = os.path.join(LOG_DIR, "app.log")

  @staticmethod
  def setup_logging():
    if not os.path.exists(ErrorHandler.LOG_DIR):
      os.makedirs(ErrorHandler.LOG_DIR)

    logger = logging.getLogger("app_logger")
    logger.setLevel(logging.ERROR)

    # Handler fichier
    file_handler = logging.FileHandler(ErrorHandler.LOG_FILE)
    file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

    # Handler console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter("%(levelname)s - %(message)s"))

    # Ajouter les handlers au logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

  # Création unique du logger
  logger = setup_logging.__func__()

  @staticmethod
  def handle(message: str, log: bool = True):
    if log:
      ErrorHandler.logger.error(message)
    DisplayError.execute(message)
