import dataclasses
from src.main.freight.cargo.packages.types.builder import PackageTypeBuilder
from src.main.freight.cargo.packages.types.interface import PackageType
from src.main.freight.cargo.metrics.dimensions import DimensionsInMetres

from src.main.freight.cargo.packages.oversize.options import (
    OversizeOption, OversizeOptions)


def dummy_pallet(name: str, max_weight: float) -> PackageType:
    builder = PackageTypeBuilder()
    builder.set_base_type("pallet")
    builder.set_name(name)
    builder.set_overrides([])
    builder.set_max_weight(max_weight)

    max_dims = DimensionsInMetres()
    max_dims.length = 1.2
    max_dims.width = 1.0
    max_dims.height = 2.0
    builder.set_max_dimensions(max_dims)

    options = [
        OversizeOption("normal", 1.0), OversizeOption("oversize", 1.5),
        OversizeOption("double", 2.0), OversizeOption("triple", 3.0)
    ]

    builder.set_oversize_options(
        OversizeOptions(default=options[0], options=options))

    return builder.build()


def dummy_full_pallet():
    return dummy_pallet(name="full", max_weight=1200)


def dummy_half_pallet():
    return dummy_pallet(name="half", max_weight=600)


@dataclasses.dataclass
class DummyPallets:
    full: PackageType = dummy_full_pallet()
    half: PackageType = dummy_half_pallet()
