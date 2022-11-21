from __future__ import annotations
from abc import ABC, abstractmethod


class NetworkPallet(ABC):
    @property
    @abstractmethod
    def barcode(self) -> str:
        ...

    @barcode.setter
    @abstractmethod
    def barcode(self, new_barcode) -> None:
        ...

    @property
    @abstractmethod
    def consignment_barcode(self) -> str:
        ...

    @consignment_barcode.setter
    @abstractmethod
    def consignment_barcode(self, new_barcode):
        ...

    @property
    @abstractmethod
    def size(self) -> str:
        ...

    @size.setter
    @abstractmethod
    def size(self, new_size: str) -> None:
        ...

    @property
    @abstractmethod
    def sizes(self) -> list[str]:
        ...

    @property
    @abstractmethod
    def type(self) -> str:
        ...

    @type.setter
    @abstractmethod
    def type(self, new_type: str) -> None:
        ...

    @property
    @abstractmethod
    def types(self) -> list[str]:
        ...

    def __eq__(self, other: NetworkPallet):
        ...
