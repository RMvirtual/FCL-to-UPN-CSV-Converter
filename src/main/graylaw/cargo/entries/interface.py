from __future__ import annotations
from abc import ABC, abstractmethod
from src.main.graylaw.cargo.packages.types.interface import PackageType


class CargoEntry(ABC):
    @property
    @abstractmethod
    def package_type(self) -> PackageType:
        ...

    @property
    @abstractmethod
    def quantity(self) -> int:
        ...

    @quantity.setter
    @abstractmethod
    def quantity(self, quantity: int) -> None:
        ...

    @property
    @abstractmethod
    def weight(self) -> float:
        ...

    @weight.setter
    @abstractmethod
    def weight(self, weight: float) -> None:
        ...

    @abstractmethod
    def set_totals(self, quantity: int, weight: float) -> None:
        ...

    @abstractmethod
    def __eq__(self, other: CargoEntry) -> bool:
        ...

    @abstractmethod
    def __iadd__(self, other: CargoEntry) -> bool:
        ...
