from src.main.file_system.file_readers import runfiles
from src.main.file_system.file_readers import json_file


def upn_api() -> dict[str, str]:
    absolute_path = runfiles.load_path("config/api/upn_api.json")

    return json_file.deserialise(absolute_path)
