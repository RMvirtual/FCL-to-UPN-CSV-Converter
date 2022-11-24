from __future__ import annotations
from abc import ABC, abstractmethod


class UPNPalletReading(ABC):
    @property
    @abstractmethod
    def size(self) -> str:
        ...

    @property
    @abstractmethod
    def type(self) -> str:
        ...

    def __eq__(self, other: UPNPalletReading):
        ...


class UPNPallet(UPNPalletReading):
    @UPNPalletReading.size.setter
    @abstractmethod
    def size(self, new_size: str) -> None:
        ...

    @UPNPalletReading.type.setter
    @abstractmethod
    def type(self, new_type: str) -> None:
        ...

    @property
    @abstractmethod
    def size_constraints(self) -> list[str]:
        ...

    @property
    @abstractmethod
    def type_constraints(self) -> list[str]:
        ...
