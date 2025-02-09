from src.application.exceptions.user_exit_exception import UserExitException
from src.application.use_cases.ask_url import AskUrl
from src.application.use_cases.display_exception import DisplayException
from src.application.use_cases.display_goodbye import DisplayGoodbye
from src.application.use_cases.display_leave import DisplayLeave
from src.application.use_cases.display_welcome import DisplayWelcome
from src.application.use_cases.fetch_data import FetchData
from src.infrastructure.external_services.api_client import ApiClient
from src.infrastructure.storage.save_file import SaveFile


class AppController:
  @staticmethod
  def run():
    try:
      DisplayWelcome.execute()

      url = AskUrl.execute()

      api_client = ApiClient()
      save_file = SaveFile()

      fetch_data = FetchData(api_client, save_file)
      fetch_data.execute(url)

      DisplayGoodbye.execute()

    except UserExitException:
      DisplayLeave.execute()

    except Exception as e:
      DisplayException.execute(str(e))


  @staticmethod
  def handle_exit():
    DisplayLeave.execute()
