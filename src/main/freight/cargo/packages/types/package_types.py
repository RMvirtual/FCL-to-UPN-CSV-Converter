from __future__ import annotations
import dataclasses
from src.main.freight.cargo.metrics.dimensions import Dimensions
from src.main.freight.cargo.packages.oversize.interface import OversizeOption
from src.main.freight.cargo.packages.types import interface


@dataclasses.dataclass
class PackageDefinitions:
    name: str = ""
    base_type: str = ""
    oversize_options: list[OversizeOption] = dataclasses.field(
        default_factory=list)
    default_oversize: OversizeOption = None
    max_dimensions: Dimensions = None
    max_weight: float = 0
    override_options: list[str] = dataclasses.field(default_factory=list)


class PackageType(interface.PackageType):
    def __init__(self, values: PackageDefinitions):
        self._name = values.name
        self._base_type = values.base_type
        self._oversize_option = values.default_oversize
        self._oversize_options = values.oversize_options
        self._max_dimensions = values.max_dimensions
        self._max_weight = values.max_weight
        self._override_options = values.override_options

    @property
    def name(self) -> str:
        return self._name

    @property
    def base_type(self) -> str:
        return self._base_type

    @property
    def oversize_option(self) -> OversizeOption:
        return self._oversize_option

    @oversize_option.setter
    def oversize_option(self, option_name: str) -> None:
        matching_options = list(filter(
            lambda option: option_name == option.name, self._oversize_options))

        if not matching_options:
            raise ValueError("Oversize option not found.")

        self._oversize_option = matching_options[0]

    @property
    def oversize_multiplier(self) -> float:
        return self._oversize_option.multiplier

    @property
    def all_oversize_options(self) -> list[OversizeOption]:
        return self._oversize_options

    @property
    def maximum_dimensions(self) -> Dimensions:
        return self._max_dimensions

    @property
    def maximum_weight(self) -> float:
        return self._max_weight

    @property
    def override_options(self):
        return self._override_options

    def __eq__(self, other: PackageType) -> bool:
        return self._name_matches(other) and self._oversize_matches(other)

    def _name_matches(self, other: PackageType) -> bool:
        return self._name == other.name

    def _oversize_matches(self, other: PackageType) -> bool:
        return self._oversize_option == other.oversize_option
