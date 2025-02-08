from src.application.controllers.app_controller import AppController


def main():
  AppController.run()

if __name__ == "__main__":
  try:
    main()

  except KeyboardInterrupt:
    AppController.handle_exit()
