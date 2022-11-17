from __future__ import annotations
from src.main.file_system.freight import cargo_types
from src.main.freight.cargo.packages.oversize import options as oversize
from src.main.freight.cargo.packages.oversize.interface import OversizeOption
from src.main.freight.cargo.packages import interface
from src.main.freight.cargo.metrics.dimensions import DimensionsInMetres


def load(package_type_name: str) -> PackageType:
    matching_types = _matching_package_types(package_type_name)

    if not matching_types:
        raise ValueError("Package type does not exist.")

    return matching_types.pop()


def _matching_package_types(type_name: str) -> list[PackageType]:
    return list(filter(
        lambda package_type: package_type.name == type_name, _package_types()))


def _package_types() -> list[PackageType]:
    return list(map(_deserialise, cargo_types.base_packages_file()))


def _deserialise(package_type_definitions: dict[str, str]) -> PackageType:
    result = PackageType()
    result.name = package_type_definitions["name"]
    result.base_type = package_type_definitions["type"]

    result.all_oversize_options = oversize.options_by_base_type(
        result.base_type)

    result.maximum_dimensions = DimensionsInMetres()
    result.maximum_dimensions.length = package_type_definitions[
        "maximum_length"]

    result.maximum_dimensions.width = package_type_definitions["maximum_width"]
    result.maximum_dimensions.height = package_type_definitions[
        "maximum_height"]

    result.maximum_weight = package_type_definitions["maximum_weight"]
    result.override_options = package_type_definitions["override_options"]

    return result


class PackageType(interface.PackageType):
    def __init__(self):
        self._name = ""
        self._base_type = None
        self._oversize_option: str = "normal"
        self._oversize_options: {str, dict[str, float]} or None = None
        self._max_dimensions = DimensionsInMetres()
        self._max_weight = None
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
    def base_type(self, new_type: str):
        self._base_type = new_type

    @property
    def oversize_option(self) -> str:
        return self._oversize_option

    @oversize_option.setter
    def oversize_option(self, new_option: str) -> None:
        if new_option in self._oversize_options:
            self._oversize_option = new_option

        else:
            raise ValueError("Oversize option not found.")

    @property
    def oversize_multiplier(self) -> float:
        return self._oversize_options[self._oversize_option]

    @property
    def all_oversize_options(self) -> list[OversizeOption]:
        return self._oversize_options

    @all_oversize_options.setter
    def all_oversize_options(self, new_options: list[OversizeOption]) -> None:
        self._oversize_options = new_options

    @property
    def maximum_dimensions(self) -> DimensionsInMetres:
        return self._max_dimensions

    @maximum_dimensions.setter
    def maximum_dimensions(self, new_dimensions: DimensionsInMetres):
        self._max_dimensions = new_dimensions

    @property
    def maximum_weight(self) -> float:
        return self._max_weight

    @maximum_weight.setter
    def maximum_weight(self, new_weight: float):
        self._max_weight = new_weight

    @property
    def override_options(self):
        return self._override_options

    @override_options.setter
    def override_options(self, new_options):
        self._override_options = new_options

    def __eq__(self, other: PackageType) -> bool:
        return self._name_matches(other) and self._oversize_matches(other)

    def _name_matches(self, other: PackageType) -> bool:
        return self._name == other.name

    def _oversize_matches(self, other: PackageType) -> bool:
        return self._oversize_option == other.oversize_option
