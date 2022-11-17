from abc import ABC, abstractmethod
from src.main.freight.cargo.metrics.interface import Dimensions
from src.main.freight.cargo.packages.oversize.interface import OversizeOption


class PackageType(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @name.setter
    @abstractmethod
    def name(self, new_name: str) -> None:
        ...

    @property
    @abstractmethod
    def base_type(self) -> str:
        ...

    @base_type.setter
    @abstractmethod
    def base_type(self, new_base_type: str) -> None:
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

    @all_oversize_options.setter
    @abstractmethod
    def all_oversize_options(self, new_options: list[OversizeOption]) -> None:
        ...

    @property
    @abstractmethod
    def maximum_dimensions(self) -> Dimensions:
        ...

    @maximum_dimensions.setter
    @abstractmethod
    def maximum_dimensions(self, new_dimensions: Dimensions) -> None:
        ...

    @property
    @abstractmethod
    def maximum_weight(self) -> float:
        ...

    @maximum_weight.setter
    @abstractmethod
    def maximum_weight(self, new_weight: float) -> None:
        ...

    @property
    @abstractmethod
    def override_options(self) -> list:
        ...

    @override_options.setter
    @abstractmethod
    def override_options(self, new_override_options) -> None:
        ...
