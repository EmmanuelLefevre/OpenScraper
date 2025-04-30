import tkinter as tk
from tkinter import filedialog
from src.application.use_cases.display_message import DisplayMessage

class AskFilePath:
  @staticmethod
  def execute(default_name: str, file_format: str) -> str | None:
    root = tk.Tk()
    root.withdraw()

    filetypes = [("JSON files", "*.json")] if file_format == "json" else [("CSV files", "*.csv")]

    DisplayMessage.message("📂 Sélectionnez un emplacement pour sauvegarder le fichier.")
    file_path = filedialog.asksaveasfilename(
      initialfile=default_name,
      defaultextension=f".{file_format}",
      filetypes=filetypes
    )

    if not file_path:
      DisplayMessage.backup_aborted()
      return None

    return file_path
