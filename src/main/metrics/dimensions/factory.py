from src.main.metrics.dimensions.implementation import DimensionsInMetres
from src.main.metrics.dimensions.interface import Dimensions


def dimensions_m3(length: float, width: float, height: float) -> Dimensions:
    result = DimensionsInMetres()
    result.length = length
    result.width = width
    result.height = height

    return result
