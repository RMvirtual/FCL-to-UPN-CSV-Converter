import dataclasses
import json

from src.main.file_system.file_readers import runfiles


@dataclasses.dataclass
class ImportStructure:
    file_path: str = ""
    field_type: type = None


def read(src: str) -> dataclasses.dataclass:
    file_path = runfiles.absolute_path(src)
    deserialise(file_path)

    return None


def deserialise(file_path: str):
    _validate_file_path(file_path)

    with open(file_path) as json_stream:
        return json.load(json_stream)


def _validate_file_path(file_path: str):
    if not type(file_path) is str:
        raise TypeError("Must be a string type file path.")

    if not file_path.lower().endswith(".json"):
        raise ValueError(
            "File must have a .json extension. Instead got" + file_path)

