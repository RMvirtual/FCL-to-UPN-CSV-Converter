from abc import ABC, abstractmethod


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
    def oversize_option(self) -> str:
        ...

    @oversize_option.setter
    @abstractmethod
    def oversize_option(self, new_oversize_option: str) -> None:
        ...

    @property
    @abstractmethod
    def oversize_multiplier(self) -> float:
        ...

    @property
    @abstractmethod
    def all_oversize_options(self) -> list:
        ...

    @all_oversize_options.setter
    @abstractmethod
    def all_oversize_options(self, new_oversize_options: list) -> None:
        ...

    @property
    @abstractmethod
    def maximum_dimensions(self) -> dict[str, float]:
        ...

    @maximum_dimensions.setter
    @abstractmethod
    def maximum_dimensions(self, new_dimensions: dict[str, float]) -> None:
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
