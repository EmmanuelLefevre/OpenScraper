import requests
from src.application.services.message_printer import MessagePrinter

class ApiClient:
  def get_data(url: str) -> dict:
    try:
      response = requests.get(url)
      response.raise_for_status()
      return response.json()

    except requests.exceptions.RequestException as e:
      MessagePrinter.print_error(str(e))
      MessagePrinter.print_error("Erreur API : {e}")
      raise RuntimeError(f"Erreur lors de la récupération des données depuis l'API : {e}")
