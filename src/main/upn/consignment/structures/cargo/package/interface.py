from __future__ import annotations
from abc import ABC, abstractmethod


class UPNPalletReading(ABC):
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

    def __eq__(self, other: UPNPalletReading):
        ...


class UPNPallet(UPNPalletReading):
    @UPNPalletReading.barcode.setter
    @abstractmethod
    def barcode(self, new_barcode) -> None:
        ...

    @UPNPalletReading.consignment_barcode.setter
    @abstractmethod
    def consignment_barcode(self, new_barcode):
        ...

    @UPNPalletReading.size.setter
    @abstractmethod
    def size(self, new_size: str) -> None:
        ...

    @property
    @abstractmethod
    def sizes(self) -> list[str]:
        ...

    @UPNPalletReading.type.setter
    @abstractmethod
    def type(self, new_type: str) -> None:
        ...

    @property
    @abstractmethod
    def types(self) -> list[str]:
        ...
