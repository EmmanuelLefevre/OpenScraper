from src.application.use_cases.display_error import DisplayError
from src.application.use_cases.display_success import DisplaySuccess
from src.infrastructure.external_services.api_client import ApiClient


class RetrieveData:
  def __init__(self, api_client: ApiClient) -> None:
    self.api_client = api_client


  def execute(self, url: str) -> dict | None:
    try:
      data = self.api_client.get_data(url)
      DisplaySuccess.execute("Données récupérées...")
      return data

    except RuntimeError as e:
      DisplayError.execute(str(e))
      return None
