from src.infrastructure.external_services.api_client import ApiClient
from src.application.services.message_printer import MessagePrinter

class RetrieveData:
  @staticmethod
  def execute(url: str):
    try:
      data = ApiClient.get_data(url)
      MessagePrinter.print_success("Données récupérées...")
      return data

    except RuntimeError as e:
      MessagePrinter.print_error(str(e))
      return None
