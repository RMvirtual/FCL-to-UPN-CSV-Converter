from abc import ABC, abstractmethod
from src.main.freight.cargo.metrics.interface import Dimensions
from src.main.freight.cargo.packages.oversize.interface import OversizeOption


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
    def oversize_option(self) -> OversizeOption:
        ...

    @oversize_option.setter
    @abstractmethod
    def oversize_option(self, option_name: str) -> None:
        ...

    @property
    @abstractmethod
    def oversize_multiplier(self) -> float:
        ...

    @property
    @abstractmethod
    def all_oversize_options(self) -> list[OversizeOption]:
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
