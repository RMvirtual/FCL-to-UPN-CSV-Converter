from src.main.freight.cargo.packages.oversize import factory as oversize
from src.main.freight.cargo.packages.types.builder import PackageTypeBuilder
from src.main.freight.cargo.packages.types.interface import PackageType
from src.main.metrics.dimensions.factory import dimensions_m3
from src.main.metrics.dimensions.interface import Dimensions


def pallet(name: str, max_weight: float, max_dims: Dimensions) -> PackageType:
    builder = PackageTypeBuilder()
    builder.set_base_type("pallet")
    builder.set_name(name)
    builder.set_overrides([])
    builder.set_max_weight(max_weight)
    builder.set_max_dimensions(max_dims)
    builder.set_oversize_options(oversize.full_options())

    return builder.build()


def full_pallet():
    return pallet("full", max_weight=1200, max_dims=dimensions_m3(1.2, 1, 2))


def half_pallet():
    return pallet("half", max_weight=600, max_dims=dimensions_m3(1.2, 1, 1))
