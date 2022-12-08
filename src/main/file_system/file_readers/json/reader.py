import json
from src.main.file_system.file_readers.json import validation


@validation.validate_json_monad
def deserialise(file_path: str) -> dict[str, any]:
    with open(file_path) as json_stream:
        return json.load(json_stream)
