from __future__ import annotations
from abc import abstractmethod
from src.main.upn.api.interfaces.pallets.upn_pallet import UPNPalletInterface


class CustPalletInterface(UPNPalletInterface):
    @abstractmethod
    def __eq__(self, other: CustPalletInterface or UPNPalletInterface):
        ...

    @property
    @abstractmethod
    def weight(self) -> int:
        ...

    @weight.setter
    @abstractmethod
    def weight(self, new_weight) -> None:
        ...
