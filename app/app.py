from app.use_cases.display_welcome import DisplayWelcome

def main():
  try:
    DisplayWelcome.execute()

  except Exception as e:
    print(f"Une erreur est survenue : {e}")

if __name__ == "__main__":
  main()
