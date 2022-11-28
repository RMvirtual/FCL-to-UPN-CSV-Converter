from src.main.metrics.dimensions.implementation import (
    Dimensions, DimensionsInMetres)

from src.main.freight.cargo.packages.oversize.implementation import (
    OversizeOptions, OversizeOption)


def dimensions(
        length: float = 1.2, width: float = 1.0, height: float = 2.0
) -> Dimensions:
    result = DimensionsInMetres()
    result.length = length
    result.width = width
    result.height = height

    return result


def oversize_options() -> OversizeOptions:
    options = [
        OversizeOption("normal", 1.0), OversizeOption("oversize", 1.5),
        OversizeOption("double", 2.0), OversizeOption("triple", 3.0)
    ]

    return OversizeOptions(default=options[0], options=options)
