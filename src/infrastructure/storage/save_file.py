import json
import pandas as pd
import os
import tkinter as tk

from io import StringIO
from src.application.use_cases.display_error import DisplayError
from src.application.use_cases.display_exception import DisplayException
from src.application.use_cases.display_saved_file_folder import DisplaySavedFileFolder
from src.application.use_cases.display_message import DisplayMessage
from src.application.use_cases.display_backup_aborted import DisplayBackupAborted
from tkinter import filedialog


class SaveFile:
  DATA_FOLDER = "data_frame"
  STORAGE_DIR = os.path.join(os.getcwd(), "src", "infrastructure", "storage")


  @staticmethod
  def ensure_data_folder_exists() -> None:
    data_frame_path = os.path.join(SaveFile.STORAGE_DIR, SaveFile.DATA_FOLDER)
    if not os.path.exists(data_frame_path):
      os.makedirs(data_frame_path)


  @staticmethod
  def save(data: str, filename: str = "data_frame") -> None:
    try:
      SaveFile.ensure_data_folder_exists()

      root = tk.Tk()
      root.withdraw()

      if "{" in data:
        filetypes = [("JSON files", "*.json")]
        extension = ".json"
      else:
        filetypes = [("CSV files", "*.csv")]
        extension = ".csv"

      DisplayMessage.execute("📂 Sélectionner un emplacement pour sauvegarder le fichier.")
      file_path = filedialog.asksaveasfilename(
        initialdir=os.path.join(SaveFile.STORAGE_DIR, SaveFile.DATA_FOLDER),
        initialfile=filename,
        defaultextension=extension,
        filetypes=filetypes
      )

      if not file_path:
        DisplayBackupAborted.execute()
        return

      if not file_path.lower().endswith(('.json', '.csv')):
        extension = "json" if "{" in data else "csv"
        file_path += f".{extension}"
      else:
        extension = "json" if file_path.endswith(".json") else "csv"

      if extension == "json":
        try:
          json_data = json.loads(data)
          with open(file_path, "w", encoding="utf-8") as file:
            json.dump(json_data, file, ensure_ascii=False, indent=2)

        except json.JSONDecodeError as e:
          DisplayError.execute(f"Erreur de décodage JSON : {e}")
          return

      elif extension == "csv":
        try:
          df = pd.read_csv(StringIO(data))

        except pd.errors.ParserError as e:
          DisplayError.execute(f"Erreur de parsing CSV : {e}")
          return

        df.to_csv(file_path, index=False, encoding="utf-8")

      folder_path, final_filename = os.path.split(file_path)
      DisplaySavedFileFolder.execute(f"{final_filename} enregistré sous => {folder_path}/")

    except PermissionError:
      DisplayError.execute("Fichier ouvert, assurez-vous que celui-ci est fermé !")
    except Exception as e:
      DisplayException.execute(f"Erreur lors de la sauvegarde : {e}")
