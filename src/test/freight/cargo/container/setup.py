from src.main.freight.cargo.container.implementation import Cargo
from src.main.freight.cargo.container.interface import Cargo as CargoInterface
from src.main.freight.cargo.entries.implementation import CargoEntry
from src.main.freight.cargo.packages.types.builder import PackageTypeBuilder
from src.main.freight.cargo.packages.types.interface import PackageType
from src.main.metrics.dimensions import factory as dims_factory


def two_entry_cargo() -> CargoInterface:
    result = Cargo()
    result.add(CargoEntry(package=full_pallet(), quantity=3, weight=3000))
    result.add(CargoEntry(package=half_pallet(), quantity=2, weight=1200))

    return result


def full_pallet() -> PackageType:
    builder = PackageTypeBuilder()
    builder.set_base_type("pallet")
    builder.set_name("full")
    builder.set_max_dimensions(dims_factory.dimensions_m3(1.2, 1.0, 2.0))
    builder.set_max_weight(1200)
    builder.set_overrides([])
    builder.set_oversize_options([])

    return builder.build()


def half_pallet() -> PackageType:
    builder = PackageTypeBuilder()
    builder.set_base_type("pallet")
    builder.set_name("half")
    builder.set_max_dimensions(dims_factory.dimensions_m3(1.2, 1.0, 1.0))
    builder.set_max_weight(600)
    builder.set_overrides([])
    builder.set_oversize_options([])

    return builder.build()
