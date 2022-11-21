from src.main.graylaw.cargo.packages.types.builder import PackageTypeBuilder
from src.main.graylaw.cargo.packages.types.interface import PackageType
from src.main.graylaw.cargo.metrics.dimensions import DimensionsInMetres
from src.main.graylaw.cargo.packages.oversize.factory import (
    OversizeOptions, OversizeOption)


def _double_half_pallet() -> PackageType:
    builder = PackageTypeBuilder()
    builder.set_base_type("pallet")
    builder.set_name("half")
    builder.set_max_weight(600)

    dims = DimensionsInMetres()
    dims.length = 1.2
    dims.width = 1.0
    dims.height = 1.0

    builder.set_max_dimensions(dims)

    builder.set_oversize_options([])

    options = [
        OversizeOption("normal", 1.0), OversizeOption("oversize", 1.5),
        OversizeOption("double", 2.0), OversizeOption("triple", 3.0)
    ]

    oversize = OversizeOptions(default=options[0], options=options)
    builder.set_oversize_options(oversize)

    result = builder.build()
    result.oversize.select("double")

    return result
