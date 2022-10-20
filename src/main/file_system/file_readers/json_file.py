import dataclasses
import json

from src.main.file_system.file_readers import runfiles


@dataclasses.dataclass
class ImportStructure:
    file_path: str = ""
    field_type: type = None


def read(src: str) -> dataclasses.dataclass:
    file_path = runfiles.load_path(src)
    json_contents(file_path)

    return None


def json_contents(file_path: str):
    with open(file_path) as json_stream:
        return json.load(json_stream)
