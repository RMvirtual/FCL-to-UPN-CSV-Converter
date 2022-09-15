from __future__ import annotations
import json
from src.main.file_system.runfiles import load_path
from src.main.freight.cargo.oversize_options import options_by_base_type


def load_package_type(type_name: str) -> PackageType or None:
    base_packages_file = load_path(
        "resources/cargo_types/base_packages.json")

    with open(base_packages_file, "r") as json_file:
        objects = json.load(json_file)

    types = []

    for package_type in objects:
        result = PackageType()
        result.name = package_type["name"]
        result.base_type = package_type["type"]

        result.all_oversize_options = options_by_base_type(
            result.base_type)

        result.maximum_dimensions = {
            "length": package_type["maximum_length"],
            "width": package_type["maximum_width"],
            "height": package_type["maximum_height"]
        }

        result.maximum_weight = package_type["maximum_weight"]
        result.override_options = package_type["override_options"]

        types.append(result)

    for package in types:
        if package.name == type_name:
            return package

    return None


class PackageType:
    def __init__(self):
        self._name = ""
        self._base_type = None
        self._oversize_option: dict[str, float] or None = None
        self._oversize_options: {str, dict[str, float]} or None = None
        self._maximum_dimensions: dict[str, float] or None = None
        self._maximum_weight = None
        self._override_options: list[str] = []

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str):
        self._name = new_name

    @property
    def base_type(self) -> str:
        return self._base_type

    @base_type.setter
    def base_type(self, new_type):
        self._base_type = new_type

    @property
    def oversize_option(self) -> dict[str, float]:
        return {
            self._oversize_option:
                self._oversize_options[self._oversize_option]
        }

    @oversize_option.setter
    def oversize_option(self, new_option: dict[str, float]):
        self._oversize_option = new_option

    def set_oversize_option(self, option: str) -> None:
        self._oversize_option = self._oversize_options[option]

    @property
    def all_oversize_options(self):
        return self._oversize_options

    @all_oversize_options.setter
    def all_oversize_options(self, new_oversize_options) -> None:
        self._oversize_options = new_oversize_options

    @property
    def maximum_dimensions(self) -> dict[str, float]:
        return self._maximum_dimensions

    @maximum_dimensions.setter
    def maximum_dimensions(self, new_dimensions: dict[str, float]):
        self._maximum_dimensions = new_dimensions

    @property
    def maximum_weight(self):
        return self._maximum_weight

    @maximum_weight.setter
    def maximum_weight(self, new_weight):
        self._maximum_weight = new_weight

    @property
    def override_options(self):
        return self._override_options

    @override_options.setter
    def override_options(self, new_options):
        self._override_options = new_options

    def __eq__(self, other: PackageType) -> bool:
        return self._is_equal(other)

    def _is_equal(self, other: PackageType) -> bool:
        return self._name_matches(other) and self._oversize_matches(other)

    def _name_matches(self, other: PackageType) -> bool:
        return self._name == other.name

    def _oversize_matches(self, other: PackageType) -> bool:
        return self._oversize_option == other.oversize_option
