from __future__ import annotations
from abc import abstractmethod
from src.main.upn.consignment.cargo.package.pallet.interface \
    import UPNPallet


class CustPallet(UPNPallet):
    def __eq__(self, other: CustPallet):
        ...

    @property
    @abstractmethod
    def weight(self) -> int:
        ...

    @weight.setter
    def weight(self, new_weight) -> None:
        ...
