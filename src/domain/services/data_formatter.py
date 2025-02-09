import requests

from src.application.use_cases.display_message import DisplayMessage


class DataFormatter:
  @staticmethod
  def detect_data_format(response: requests.Response) -> str:
    content_type = response.headers.get("Content-Type", "").lower()

    if "application/json" in content_type:
      DisplayMessage.info("Format détecté : JSON")
      return "json"

    elif "text/csv" in content_type or "application/csv" in content_type:
      DisplayMessage.info("Format détecté : CSV")
      return "csv"

    return DataFormatter._detect_format_fallback(response.text)


  @staticmethod
  def _detect_format_fallback(content: str) -> str:
    try:
      requests.models.json.loads(content)
      DisplayMessage.info("Format détecté : JSON")
      return "json"

    except ValueError:
      pass

    delimiters = [",", ";", "\t", "|", ":", "#", "/", "\\"]

    if any(delim in content for delim in delimiters):
      DisplayMessage.info("Format détecté : CSV")
      return "csv"

    DisplayMessage.error("Format de données inconnu !")
    return "unknown"
