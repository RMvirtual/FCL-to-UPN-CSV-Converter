from src.main.freight.cargo.packages.types.interface import PackageType
from src.main.freight.cargo.entries.implementation import CargoEntry
from src.main.freight.cargo.packages.types import factory


def entry(
        package: PackageType, quantity: int, weight: float,
        oversize: str = None
) -> CargoEntry:
    result = CargoEntry(package, quantity, weight)

    if oversize:
        result.package_type.oversize.select(oversize)

    return result


def full_pallet_entry(
        quantity: int, weight: float, oversize: str = None) -> CargoEntry:
    return entry(factory.full_pallet(), quantity, weight, oversize)


def half_pallet_entry(
        quantity: int, weight: float, oversize: str = None) -> CargoEntry:
    return entry(factory.half_pallet(), quantity, weight, oversize)
