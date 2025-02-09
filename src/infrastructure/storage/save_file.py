class SaveFile:
  @staticmethod
  def save(data: str, filename: str) -> None:
    with open(filename, "w", encoding="utf-8") as file:
      file.write(data)
