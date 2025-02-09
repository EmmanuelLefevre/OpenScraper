from src.application.exceptions.user_exit_exception import UserExitException
from src.application.use_cases.ask_url import AskUrl
from src.application.use_cases.display_exception import DisplayException
from src.application.use_cases.display_goodbye import DisplayGoodbye
from src.application.use_cases.display_leave import DisplayLeave
from src.application.use_cases.display_warning import DisplayWarning
from src.application.use_cases.retrieve_data import RetrieveData
from src.application.use_cases.display_welcome import DisplayWelcome
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
      retrieve_data = RetrieveData(api_client, save_file)
      data = retrieve_data.execute(url)
      print(data)

      DisplayGoodbye.execute()

    except UserExitException:
      DisplayLeave.execute()

    except Exception as e:
      DisplayException.execute(str(e))


  @staticmethod
  def handle_exit():
    DisplayLeave.execute()
