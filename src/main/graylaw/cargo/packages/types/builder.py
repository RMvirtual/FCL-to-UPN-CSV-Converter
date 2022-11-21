from src.main.graylaw.cargo.packages.types.package_types import (
    PackageType, PackageDefinitions)

from src.main.graylaw.cargo.packages.types.interface import Dimensions
from src.main.graylaw.cargo.packages.oversize.interface import OversizeOptions


class PackageTypeBuilder:
    def __init__(self):
        self._definitions = PackageDefinitions()

    def build(self) -> PackageType:
        return PackageType(self._definitions)

    def reset(self) -> None:
        self._definitions = PackageDefinitions()

    def set_name(self, name: str) -> None:
        self._definitions.name = name

    def set_base_type(self, base_type: str) -> None:
        self._definitions.base_type = base_type

    def set_oversize_options(self, options: OversizeOptions) -> None:
        self._definitions.oversize_options = options

    def set_max_dimensions(self, dimensions: Dimensions) -> None:
        self._definitions.max_dimensions = dimensions

    def set_max_weight(self, weight: float) -> None:
        self._definitions.max_weight = weight

    def set_overrides(self, overrides: list[str]) -> None:
        self._definitions.override_options = overrides
