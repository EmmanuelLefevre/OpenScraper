import requests

from src.application.use_cases.display_exception import DisplayException
from src.domain.services.data_formatter import DataFormatter


class ApiClient:
  @staticmethod
  def get_data(url: str) -> str | None:
    try:
      response = requests.get(url, timeout=10)
      response.raise_for_status()

      return DataFormatter.format_response(response)

    except requests.exceptions.RequestException as e:
      DisplayException.execute(str(e))
      return None
