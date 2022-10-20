import json
from src.main.file_system.file_readers import runfiles


def load_path(file_name: str):
    sys_files = _json_contents()
    result = None

    for file in sys_files:
        if file == file_name:
            result = sys_files[file]
            break

    if result is None:
        raise ValueError("No file found matching", file_name)

    return result


def _json_contents():
    with open(_file_path()) as json_file:
        return json.load(json_file)


def _file_path():
    return runfiles.absolute_path("resources/file_system.json")
