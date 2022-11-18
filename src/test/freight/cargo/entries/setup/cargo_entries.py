from src.main.freight.cargo.packages.types.interface import PackageType
from src.main.freight.cargo.entries.entry import CargoEntry


def entry(
        pkg_type: PackageType, qty_and_weight: tuple[int, float]) -> CargoEntry:
    result = CargoEntry(pkg_type)
    result.quantity_and_weight = qty_and_weight

    return result
