from abc import ABC, abstractmethod
from src.main.metrics.dimensions.interface import Dimensions
from src.main.freight.cargo.packages.oversize.interface import OversizeOptions


class PackageType(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @property
    @abstractmethod
    def base_type(self) -> str:
        ...

    @property
    @abstractmethod
    def oversize(self) -> OversizeOptions:
        ...

    @property
    @abstractmethod
    def maximum_dimensions(self) -> Dimensions:
        ...

    @property
    @abstractmethod
    def maximum_weight(self) -> float:
        ...

    @property
    @abstractmethod
    def override_options(self) -> list:
        ...
