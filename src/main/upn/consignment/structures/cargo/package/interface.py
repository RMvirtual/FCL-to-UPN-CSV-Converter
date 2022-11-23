from __future__ import annotations
from abc import ABC, abstractmethod


class UPNPallet(ABC):
    @property
    @abstractmethod
    def barcode(self) -> str:
        ...

    @property
    @abstractmethod
    def consignment_barcode(self) -> str:
        ...

    @property
    @abstractmethod
    def size(self) -> str:
        ...

    @property
    @abstractmethod
    def type(self) -> str:
        ...

    def __eq__(self, other: UPNPallet):
        ...
