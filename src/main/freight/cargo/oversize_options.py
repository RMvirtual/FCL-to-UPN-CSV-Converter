from __future__ import annotations
from src.main.file_system.file_readers import runfiles
from src.main.file_system.file_readers import json_file


def all_options() -> dict[str, dict[str, float]]:
    result = {}
    options_file = option_file_contents()

    for entry in options_file:
        package_type = entry["base_type"]
        package_type_options = _package_type_from_json(entry)
        result[package_type] = package_type_options

    return result


def option_file_contents() -> list[dict[str, str]]:
    options_file = runfiles.absolute_path(
        "resources/cargo_types/oversize_options.json")

    return json_file.deserialise(options_file)


def _package_type_from_json(json_entry):
    result = {}

    for option in json_entry["options"]:
        result[option["name"]] = option["multiplier"]

    return result


def options_by_base_type(base_type: str):
    result = None
    options = all_options()

    for option in options:
        if option == base_type:
            result = options[base_type]
            break

    return result

