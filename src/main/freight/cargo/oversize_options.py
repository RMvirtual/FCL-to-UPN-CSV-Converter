from __future__ import annotations
import json
from src.main.file_system.runfiles import load_path


def load_options_by_base_type(base_type: str):
    oversize_options = load_all_options()
    filtered_options = {}

    for key, value in oversize_options:
        if base_type in value.multiplier:
            filtered_options[key] = value

    return filtered_options


def load_all_options() -> OversizeOptions:
    options_file = load_from_json()
    options = OversizeOptions()

    for option in options_file:
        result = OversizeOption()
        result.name = option["name"]
        result.multiplier = option["package_type_multipliers"]
        options[result.name] = result

    return options


def load_option(option_name: str):
    options = load_from_json()
    result = None

    for option in options:
        if option["name"] == option_name:
            result = OversizeOption()
            result.name = option["name"]
            result.multiplier = option["package_type_multipliers"]
            break

    return result


def load_from_json() -> list[dict[str, str]]:
    options_file = load_path(
        "resources/cargo_types/oversize_options.json")

    with open(options_file, "r") as json_file:
        result = json.load(json_file)

    return result


class OversizeOptions:
    def __init__(self):
        self._options: dict[str, OversizeOption] = {}
        self._default: OversizeOption or None = None

    def __setitem__(self, option_name: str, option: OversizeOption) -> None:
        self._options[option_name] = option

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
