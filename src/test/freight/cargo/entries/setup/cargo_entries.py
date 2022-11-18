from src.main.freight.cargo.packages.types.interface import PackageType
from src.main.freight.cargo.entries.entry import CargoEntry
from src.test.freight.cargo.entries.setup import packages


def entry(
        pkg_type: PackageType, qty_and_weight: tuple[int, float],
        oversize_option: str = None
) -> CargoEntry:
    result = CargoEntry(pkg_type)
    result.quantity_and_weight = qty_and_weight

    if oversize_option:
        result.package_type.oversize.select(oversize_option)

    return result


def full_pallet_entry(
        quantity: int, weight: float, oversize: str = None) -> CargoEntry:
    return entry(
        pkg_type=packages.DummyPallets.full,
        qty_and_weight=(quantity, weight),
        oversize_option=oversize
    )


def half_pallet_entry(
        quantity: int, weight: float, oversize: str = None) -> CargoEntry:
    return entry(
        pkg_type=packages.DummyPallets.half,
        qty_and_weight=(quantity, weight),
        oversize_option=oversize
    )
