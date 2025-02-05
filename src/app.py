from src.application.use_cases.ask_url import AskUrl
# from src.application.use_cases.display_error import DisplayError
from src.application.use_cases.display_goodbye import DisplayGoodbye
from src.application.use_cases.display_leave import DisplayLeave
from src.application.use_cases.display_welcome import DisplayWelcome
from src.application.services.error_handler import ErrorHandler

def main():
  try:
    DisplayWelcome.execute()
    url = AskUrl.execute()
    DisplayGoodbye.execute()

  except Exception as e:
    # DisplayError.execute(str(e))
    ErrorHandler.handle(e)

if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    DisplayLeave.execute()
  except Exception as e:
    ErrorHandler.handle(e)
