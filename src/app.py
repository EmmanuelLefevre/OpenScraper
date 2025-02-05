from src.application.use_cases.display_goodbye import DisplayGoodbye
from src.application.use_cases.display_leave import DisplayLeave
from src.application.use_cases.display_welcome import DisplayWelcome

def main():
  try:
    DisplayWelcome.execute()
    DisplayGoodbye.execute()

  except Exception as e:
    print(f"Une erreur est survenue : {e}")

if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    DisplayLeave.execute()