import requests

from src.application.use_cases.display_error import DisplayError
from src.application.use_cases.display_exception import DisplayException
from src.domain.services.data_extractor import DataExtractor
from src.domain.services.data_formatter import DataFormatter


class ApiClient:
  @staticmethod
  def get_data(url: str) -> str | None:
    try:
      response = requests.get(url, timeout=10)
      response.raise_for_status()

      data_format = DataFormatter.detect_data_format(response)

      if data_format == "json":
        return DataExtractor.extract_from_json(response.text)

      elif data_format == "csv":
        return response.text

      else:
        DisplayError.execute("Format de données non pris en charge.")
        return None

    except requests.exceptions.RequestException as e:
      DisplayException.execute(str(e))
      return None
