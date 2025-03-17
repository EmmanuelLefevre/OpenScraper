from src.application.exceptions.user_exit_exception import UserExitException
from src.application.use_cases.ask_url import AskUrl
from src.application.use_cases.display_message import DisplayMessage
from src.application.use_cases.fetch_data import FetchData
from src.infrastructure.external_services.api_client import ApiClient
from src.infrastructure.storage.save_file import SaveFile


class AppController:
  @staticmethod
  def run():
    try:
      DisplayMessage.welcome()

      url = AskUrl.execute()

      api_client = ApiClient()
      save_file = SaveFile()

      fetch_data = FetchData(api_client, save_file)
      fetch_data.execute(url)

      DisplayMessage.goodbye()

    except UserExitException:
      DisplayMessage.leave()

    except Exception as e:
      DisplayMessage.exception(str(e))


  @staticmethod
  def handle_exit():
    DisplayMessage.leave()
