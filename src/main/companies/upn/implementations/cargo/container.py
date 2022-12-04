from src.main.companies.upn.interfaces.pallets import UPNPallet
from src.main.companies.upn.interfaces.cargo import UPNCargo as UPNCargoable


class UPNCargo(UPNCargoable):
    def __init__(self):
        self._total_weight = 0
        self._pallets = []

    @property
    def total_weight(self) -> int:
        return self._total_weight

    @property
    def pallets(self) -> list[UPNPallet]:
        return self._pallets

