from abc import ABC, abstractmethod
from src.main.graylaw.cargo.entries.interface import CargoEntry
from src.main.graylaw.cargo.packages.types.interface import PackageType


class CargoReading(ABC):
    @abstractmethod
    def __contains__(self, entry: CargoEntry) -> bool:
        ...

    @abstractmethod
    def __iter__(self):
        ...

    @abstractmethod
    def __getitem__(self, index: int) -> CargoEntry:
        ...

    @abstractmethod
    def __len__(self) -> int:
        ...

    @abstractmethod
    def index_by_package_type(self, package_type: PackageType) -> CargoEntry:
        ...

    @property
    @abstractmethod
    def total_weight(self) -> float:
        ...


class Cargo(CargoReading):
    @abstractmethod
    def add(self, entry: CargoEntry) -> None:
        ...

    @abstractmethod
    def clear(self) -> None:
        ...

