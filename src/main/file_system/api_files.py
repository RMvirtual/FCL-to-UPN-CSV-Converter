import json
from src.main.file_system import runfiles


def upn_api() -> dict[str, str]:
    return deserialise_json_file("config/api/upn_api.json")


def deserialise_json_file(src_path: str) -> dict[str, str]:
    with open(runfiles.load_path(src_path)) as file_stream:
        return json.load(file_stream)
