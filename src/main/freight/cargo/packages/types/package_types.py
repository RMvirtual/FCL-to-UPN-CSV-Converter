import dataclasses
from src.main.freight.cargo.metrics.dimensions import Dimensions
from src.main.freight.cargo.packages.oversize.interface import OversizeOptions
from src.main.freight.cargo.packages.types import interface


@dataclasses.dataclass
class PackageDefinitions:
    name: str = ""
    base_type: str = ""
    oversize_options: OversizeOptions = None
    max_dimensions: Dimensions = None
    max_weight: float = 0
    override_options: list[str] = dataclasses.field(default_factory=list)


class PackageType(interface.PackageType):
    def __init__(self, values: PackageDefinitions):
        self._name = values.name
        self._base_type = values.base_type
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
    def oversize(self) -> OversizeOptions:
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

    def __eq__(self, other: interface.PackageType) -> bool:
        return self._name_matches(other) and self._oversize_matches(other)

    def _name_matches(self, other: interface.PackageType) -> bool:
        return self._name == other.name

    def _oversize_matches(self, other: interface.PackageType) -> bool:
        return self.oversize.selected == other.oversize.selected
