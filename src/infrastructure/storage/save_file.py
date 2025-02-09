import json
import pandas as pd
import os
import tkinter as tk

from src.application.use_cases.display_error import DisplayError
from src.application.use_cases.display_exception import DisplayException
from src.application.use_cases.display_saved_file_folder import DisplaySavedFileFolder
from src.application.use_cases.display_message import DisplayMessage
from src.application.use_cases.display_backup_aborted import DisplayBackupAborted
from tkinter import filedialog


class SaveFile:
  DATA_FOLDER = "data_frame"

  @staticmethod
  def ensure_data_folder_exists():
    if not os.path.exists(SaveFile.DATA_FOLDER):
      os.makedirs(SaveFile.DATA_FOLDER)


  @staticmethod
  def save(data: str, filename: str) -> None:
    try:
      root = tk.Tk()
      root.withdraw()

      DisplayMessage.execute("📂 Sélectionner un emplacement pour sauvegarder le fichier.")
      file_path = filedialog.asksaveasfilename(
        initialdir=SaveFile.DATA_FOLDER,
        initialfile=filename,
        defaultextension="",
        filetypes=[("JSON files", "*.json"), ("CSV files", "*.csv")]
      )

      if not file_path:
        DisplayBackupAborted.execute()
        return

      # Vérification et ajout automatique de l'extension
      if not file_path.lower().endswith(('.json', '.csv')):
        extension = "json" if "{" in data else "csv"
        file_path += f".{extension}"
      else:
        extension = "json" if file_path.endswith(".json") else "csv"

      # Sauvegarde du fichier
      if extension == "json":
        with open(file_path, "w", encoding="utf-8") as file:
          json.dump(json.loads(data), file, ensure_ascii=False, indent=2)
      else:
        df = pd.read_csv(pd.compat.StringIO(data))
        df.to_csv(file_path, index=False, encoding="utf-8")

      folder_path, final_filename = os.path.split(file_path)
      DisplaySavedFileFolder.execute(f"📄 {final_filename} enregistré sous => {folder_path}/")

    except PermissionError:
      DisplayError.execute("Fichier ouvert, assurez-vous que celui-ci est fermé !")
    except Exception as e:
      DisplayException.execute(f"Erreur lors de la sauvegarde : {e}")
