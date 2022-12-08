from __future__ import annotations

from abc import abstractmethod
from src.main.companies.upn.api.interface.pallets.base import UPNPallet


class UploadPallet(UPNPallet):
    @abstractmethod
    def __eq__(self, other: UploadPallet or UPNPallet):
        ...

    @property
    @abstractmethod
    def weight(self) -> int:
        ...

    @weight.setter
    @abstractmethod
    def weight(self, new_weight: int) -> None:
        ...
