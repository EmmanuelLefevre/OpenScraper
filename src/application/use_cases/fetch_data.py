from src.application.use_cases.display_message import DisplayMessage
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
        self.save_file.save(data)
      return data

    except RuntimeError as e:
      DisplayMessage.error(str(e))
      return None
