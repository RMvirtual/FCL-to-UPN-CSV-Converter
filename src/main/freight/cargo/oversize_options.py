from __future__ import annotations
import json
from src.main.file_system.runfiles import load_path


def load_oversize_options():
    base_packages_file = load_path(
        "resources/cargo_types/oversize_options.json")

    with open(base_packages_file, "r") as json_file:
        options_file = json.load(json_file)

    options = {}

    for option in options_file:
        result = OversizeOption()
        result.name = option["name"]
        result.package_multipliers = option["package_type_multipliers"]
        options[result.name] = result

    return options


def load_oversize_option(option_name: str):
    base_packages_file = load_path(
        "resources/cargo_types/oversize_options.json")

    with open(base_packages_file, "r") as json_file:
        options = json.load(json_file)

    result = None

    for option in options:
        if option["name"] == option_name:
            result = OversizeOption()
            result.name = option["name"]
            result.package_multipliers = option["package_type_multipliers"]
            break

    return result


class OversizeOption:
    def __init__(self):
        self._name: str = ""
        self._package_multipliers: dict[str, float] = {}

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_option: str) -> None:
        self._name = new_option

    @property
    def package_multipliers(self) -> dict[str, float]:
        return self._package_multipliers

    @package_multipliers.setter
    def package_multipliers(self, new_multipliers: dict[str, float]) -> None:
        self._package_multipliers = new_multipliers

    def __getitem__(self, option_name: str) -> float:
        return self._package_multipliers[option_name]

    def __eq__(self, other: OversizeOption) -> bool:
        return self._name == other.name
