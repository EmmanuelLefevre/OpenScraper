from src.application.use_cases.display_error import DisplayError
from src.application.use_cases.display_success import DisplaySuccess
from src.infrastructure.external_services.api_client import ApiClient
from src.infrastructure.storage.save_file import SaveFile


class FetchData:
  def __init__(self, api_client: ApiClient, save_file: SaveFile) -> None:
    self.api_client = api_client
    self.save_file = save_file


  def execute(self, url: str) -> str | None:
    try:
      data = self.api_client.get_data(url)
      if data:
        filename = "output.json" if "{" in data else "output.csv"
        self.save_file.save(data, filename)
        DisplaySuccess.execute(f"Données sauvegardées dans {filename}...")
      return data

    except RuntimeError as e:
      DisplayError.execute(str(e))
      return None
