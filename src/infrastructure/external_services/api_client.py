import requests

from src.application.use_cases.display_exception import DisplayException

class ApiClient:
  def get_data(url: str) -> dict:
    try:
      response = requests.get(url, timeout=10)
      response.raise_for_status()
      return response.json()

    except requests.exceptions.RequestException as e:
      DisplayException.execute(str(e))
