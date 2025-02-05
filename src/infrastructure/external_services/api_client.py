import requests

from src.application.use_cases.display_error import DisplayError

class ApiClient:
  def get_data(url: str) -> dict:
    try:
      response = requests.get(url)
      response.raise_for_status()
      return response.json()

    except requests.exceptions.RequestException as e:
      DisplayError.execute(str(e))
