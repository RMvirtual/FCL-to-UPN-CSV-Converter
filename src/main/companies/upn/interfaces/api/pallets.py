from __future__ import annotations

from abc import ABC, abstractmethod


class UPNPallet(ABC):
    @property
    @abstractmethod
    def size(self) -> str:
        """Size code."""
        ...

    @property
    @abstractmethod
    def type(self) -> str:
        """Type Code"""
        ...

    def __eq__(self, other: UPNPallet):
        ...

    @size.setter
    @abstractmethod
    def size(self, new_size: str) -> None:
        """Sets the size code."""
        ...

    @type.setter
    @abstractmethod
    def type(self, new_type: str) -> None:
        """Sets the type code."""
        ...

    @property
    @abstractmethod
    def size_constraints(self) -> list[str]:
        """The list of valid size codes."""
        ...

    @property
    @abstractmethod
    def type_constraints(self) -> list[str]:
        """The list of valid type codes."""
        ...


class NetworkPallet(UPNPallet):
    """Interface for a Network Pallet."""
    @property
    @abstractmethod
    def barcode(self) -> str:
        ...

    @barcode.setter
    @abstractmethod
    def barcode(self, new_barcode: str) -> None:
        ...

    @property
    @abstractmethod
    def consignment_barcode(self) -> str:
        ...

    @consignment_barcode.setter
    @abstractmethod
    def consignment_barcode(self, new_barcode: str) -> None:
        ...

    @abstractmethod
    def __eq__(self, other: NetworkPallet) -> bool:
        ...


class CustPallet(UPNPallet):
    @abstractmethod
    def __eq__(self, other: CustPallet or UPNPallet):
        ...

    @property
    @abstractmethod
    def weight(self) -> int:
        ...

    @weight.setter
    @abstractmethod
    def weight(self, new_weight: int) -> None:
        ...
