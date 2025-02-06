from src.application.use_cases.ask_url import AskUrl
from src.application.use_cases.display_exception import DisplayException
from src.application.use_cases.display_goodbye import DisplayGoodbye
from src.application.use_cases.display_leave import DisplayLeave
from src.application.use_cases.display_welcome import DisplayWelcome

def main():
  try:
    DisplayWelcome.execute()
    url = AskUrl.execute()
    DisplayGoodbye.execute()

  except Exception as e:
    DisplayException.execute(str(e))

if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    DisplayLeave.execute()
