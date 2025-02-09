import json

from src.application.use_cases.display_exception import DisplayException


class DataExtractor:
  @staticmethod
  def extract_from_json(response_json: str) -> str:
    try:
      parsed_json = json.loads(response_json)
      extracted_data = parsed_json.get("data", parsed_json)
      return json.dumps(extracted_data, ensure_ascii=False, indent=2)

    except json.JSONDecodeError as e:
      DisplayException.execute(str(e))
      return None
