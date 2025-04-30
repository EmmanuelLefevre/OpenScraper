from src.application.use_cases.display_message import DisplayMessage
from src.infrastructure.external_services.api_client import ApiClient
from src.infrastructure.storage.save_file import SaveFile

class FetchMoreData:
  def __init__(self, api_client: ApiClient, save_file: SaveFile) -> None:
    self.api_client = api_client
    self.save_file = save_file

  def execute(self, initial_url: str) -> None:
    next_url = initial_url

    while next_url:
      data, next_url = self.api_client.get_data_with_pagination(next_url)
      if data:
        self.save_file.save(data)
        DisplayMessage.info("D'autres résultats sont disponibles !")
        user_choice = input("Voulez-vous les télécharger ? (o/n) ").strip().lower()
        if user_choice != 'o':
          break

    DisplayMessage.data_saved()
