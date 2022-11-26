from __future__ import annotations
from abc import abstractmethod

from src.main.upn.consignment.cargo.package.pallet.interface import (
    UPNPallet, UPNPalletReading)


class NetworkPallet(UPNPallet):
    """Interface for a Network Pallet."""
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
    def consignment_barcode(self, new_barcode) -> None:
        ...

    @abstractmethod
    def __eq__(self, other: NetworkPallet or UPNPalletReading) -> bool:
        ...
