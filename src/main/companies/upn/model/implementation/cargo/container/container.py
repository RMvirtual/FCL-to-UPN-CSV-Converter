from src.main.companies.upn.api.interface.cargo.pallets.base import UPNPallet
from src.main.companies.upn.api.interface.cargo.container.cargo \
    import UPNCargo as UPNCargoable


class UPNCargo(UPNCargoable):
    def __init__(self):
        self._total_weight = 0
        self._pallets = []

    @property
    def total_weight(self) -> int:
        return self._total_weight

    @total_weight.setter
    def total_weight(self, new_weight: int) -> None:
        self._total_weight = new_weight

    @property
    def pallets(self) -> list[UPNPallet]:
        return self._pallets

    def add(self, new_pallet: UPNPallet, weight: int) -> None:
        self._pallets.append(new_pallet)
        self._total_weight += weight

