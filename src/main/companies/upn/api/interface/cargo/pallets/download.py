from __future__ import annotations

from abc import abstractmethod
from src.main.companies.upn.api.interface.cargo.pallets.base import UPNPallet


class DownloadPallet(UPNPallet):
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
    def __eq__(self, other: DownloadPallet) -> bool:
        ...
