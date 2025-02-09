import json
import requests


class DataFormatter:
  @staticmethod
  def format_response(response: requests.Response) -> str:
    content_type = response.headers.get("Content-Type", "")

    if "application/json" in content_type:
      return json.dumps(response.json(), indent=4, ensure_ascii=False)

    elif "text/csv" in content_type or "application/csv" in content_type:
      return response.text

    else:
      raise ValueError("Format de réponse non supporté")
