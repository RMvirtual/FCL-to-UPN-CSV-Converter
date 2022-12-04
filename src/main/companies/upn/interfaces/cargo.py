from abc import ABC, abstractmethod
from src.main.companies.upn.interfaces.pallets import UPNPallet


class UPNCargo(ABC):
    @property
    @abstractmethod
    def total_weight(self) -> int:
        ...

    @property
    @abstractmethod
    def pallets(self) -> list[UPNPallet]:
        ...
