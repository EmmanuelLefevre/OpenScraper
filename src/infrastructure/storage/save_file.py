import json
import pandas as pd
import os
import tkinter as tk

from src.application.use_cases.display_exception import DisplayException
from src.application.use_cases.display_message import DisplayMessage
from src.application.use_cases.display_success import DisplaySuccess
from tkinter import filedialog


class SaveFile:
  DATA_FOLDER = "data_frame"

  @staticmethod
  def ensure_data_folder_exists():
    if not os.path.exists(SaveFile.DATA_FOLDER):
      os.makedirs(SaveFile.DATA_FOLDER)


  @staticmethod
  def save(data: str, filename: str) -> None:
    with open(filename, "w", encoding="utf-8") as file:
      file.write(data)
