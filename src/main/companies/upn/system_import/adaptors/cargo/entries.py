import copy
from src.main.freight.cargo.entries.interface import CargoEntry
from src.main.freight.cargo.packages.types.interface import PackageType
from src.main.companies.upn.api.interface.pallets.base import UPNPallet


class UPNCargoEntryAdaptor(CargoEntry):
    """Adaptor for a UPN list of pallets into a house-system Cargo
    Entry.
    """
    def __init__(self, pallets: list[UPNPallet], total_weight: int):
        self._upn_pallets = copy.deepcopy(pallets)
        self._weight = total_weight

    @property
    def package_type(self) -> PackageType:
        pass

    @property
    def quantity(self) -> int:
        return len(self._upn_pallets)

    @property
    def weight(self) -> float:
        return self._weight

    def set_totals(self, quantity: int, weight: float) -> None:
        pass

    def __eq__(self, other: CargoEntry) -> bool:
        pass

    def __iadd__(self, other: CargoEntry) -> bool:
        pass

