from __future__ import annotations
from abc import abstractmethod
from src.main.upn.consignment.cargo.package.pallet.interface import UPNPallet


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
    def weight(self, new_weight) -> None:
        ...
