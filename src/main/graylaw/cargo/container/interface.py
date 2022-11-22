from abc import ABC, abstractmethod
from src.main.graylaw.cargo.entries.interface import CargoEntry


class Cargo(ABC):
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
    def add(self, entry: CargoEntry) -> None:
        ...

    @abstractmethod
    def clear(self) -> None:
        ...
