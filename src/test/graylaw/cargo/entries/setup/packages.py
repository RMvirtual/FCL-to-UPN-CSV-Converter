import dataclasses
from src.main.graylaw.cargo.packages.types.builder import PackageTypeBuilder
from src.main.graylaw.cargo.packages.types.interface import PackageType

from src.main.metrics.dimensions import (
    DimensionsInMetres, Dimensions)

from src.main.graylaw.cargo.packages.oversize.options import (
    OversizeOption, OversizeOptions)


def dummy_pallet(
        name: str, max_weight: float, max_dimensions: Dimensions
) -> PackageType:
    builder = PackageTypeBuilder()
    builder.set_base_type("pallet")
    builder.set_name(name)
    builder.set_overrides([])
    builder.set_max_weight(max_weight)
    builder.set_max_dimensions(max_dimensions)

    options = [
        OversizeOption("normal", 1.0), OversizeOption("oversize", 1.5),
        OversizeOption("double", 2.0), OversizeOption("triple", 3.0)
    ]

    builder.set_oversize_options(
        OversizeOptions(default=options[0], options=options))

    return builder.build()


def dummy_dimensions(length: float, width: float, height: float) -> Dimensions:
    result = DimensionsInMetres()
    result.length = length
    result.width = width
    result.height = height

    return result


def dummy_full_pallet():
    return dummy_pallet(
        name="full", max_weight=1200,
        max_dimensions=dummy_dimensions(1.2, 1, 2)
    )


def dummy_half_pallet():
    return dummy_pallet(
        name="half", max_weight=600,
        max_dimensions=dummy_dimensions(1.2, 1, 1)
    )


@dataclasses.dataclass
class DummyPallets:
    full: PackageType = dummy_full_pallet()
    half: PackageType = dummy_half_pallet()
