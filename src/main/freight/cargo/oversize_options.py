from __future__ import annotations
import json
from src.main.file_system.runfiles import load_path


def load_options_by_base_type(base_type: str):
    oversize_options = load_all_options()
    filtered_options = {}

    for key, value in oversize_options:
        if base_type in key:
            filtered_options[key] = value

    return filtered_options


def load_all_options() -> dict[str, OversizeOptions]:
    options_file = load_from_json()
    all_options = {}

    for entry in options_file:
        base_type = entry["base_type"]
        oversize_options = entry["options"]

        all_base_types_options = OversizeOptions()

        for option in oversize_options:
            new_option = OversizeOption()
            new_option.name = option["name"]
            new_option.multiplier = option["multiplier"]

            all_base_types_options.add(new_option)

        all_options[base_type] = all_base_types_options

    return all_options


def load_from_json() -> list[dict[str, str]]:
    options_file = load_path(
        "resources/cargo_types/oversize_options.json")

    with open(options_file, "r") as json_file:
        result = json.load(json_file)

    return result


class OversizeOption:
    def __init__(self):
        self._name: str = ""
        self._multiplier: float = 1

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_option: str) -> None:
        self._name = new_option

    @property
    def multiplier(self) -> float:
        return self._multiplier

    @multiplier.setter
    def multiplier(self, new_multiplier: float) -> None:
        self._multiplier = new_multiplier

    def __eq__(self, other: OversizeOption) -> bool:
        return (
            self._name == other.name and self._multiplier == other.multiplier)


class OversizeOptions:
    def __init__(self):
        self._options: dict[str, OversizeOption] = {}
        self._default: OversizeOption or None = None

    def add(self, option: OversizeOption) -> None:
        self._options[option.name] = option

    def __getitem__(self, option_name: str) -> OversizeOption:
        return self._options[option_name]

    @property
    def default(self) -> OversizeOption:
        return self._default

    @default.setter
    def default(self, option_name: str):
        if option_name in self._options:
            self._default = self._options[option_name]

        else:
            raise ValueError("Requested default option not found.")

