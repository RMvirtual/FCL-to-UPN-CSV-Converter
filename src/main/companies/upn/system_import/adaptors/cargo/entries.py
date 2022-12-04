import functools
from src.main.freight.cargo.entries.interface import CargoEntry
from src.main.freight.cargo.packages.types.interface import PackageType


class UPNCargoEntryAdaptor(CargoEntry):
    """Adaptor for a UPN list of pallets into a house-system Cargo
    Entry.
    """
    def __init__(self, pallets: list):
        ...

    @property
    def package_type(self) -> PackageType:
        pass

    @property
    def quantity(self) -> int:
        pass

    @property
    def weight(self) -> float:
        pass

    def set_totals(self, quantity: int, weight: float) -> None:
        pass

    def __eq__(self, other: CargoEntry) -> bool:
        pass

    def __iadd__(self, other: CargoEntry) -> bool:
        pass

