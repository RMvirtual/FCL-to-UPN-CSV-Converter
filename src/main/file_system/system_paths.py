import json
from src.main.file_system import runfiles


def load_file(file_name: str):
    all_paths_file = runfiles.load_path("resources/file_system.json")

    with open(all_paths_file) as file_paths:
        items = json.load(file_paths)

    for item in items:
        if item == file_name:
            return items[item]

    return None
