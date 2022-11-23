from __future__ import annotations
from abc import abstractmethod
from src.main.upn.consignment.structures.cargo.package.interface \
    import UPNPallet


class NetworkPallet(UPNPallet):
    @UPNPallet.barcode.setter
    @abstractmethod
    def barcode(self, new_barcode) -> None:
        ...

    @UPNPallet.consignment_barcode.setter
    @abstractmethod
    def consignment_barcode(self, new_barcode):
        ...

    @UPNPallet.size.setter
    @abstractmethod
    def size(self, new_size: str) -> None:
        ...

    @property
    @abstractmethod
    def sizes(self) -> list[str]:
        ...

    @UPNPallet.type.setter
    @abstractmethod
    def type(self, new_type: str) -> None:
        ...

    @property
    @abstractmethod
    def types(self) -> list[str]:
        ...
