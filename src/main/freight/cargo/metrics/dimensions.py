from src.main.freight.cargo.metrics.interface import Dimensions


class DimensionsInMetres(Dimensions):
    def __init__(self):
        self._length = 0
        self._width = 0
        self._height = 0

    @property
    def length(self) -> float:
        return self._length

    @length.setter
    def length(self, new_length: float) -> None:
        self._raise_exception_if_invalid_dimension(new_length)
        self._length = new_length

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, new_width: float) -> None:
        self._raise_exception_if_invalid_dimension(new_width)
        self._width = new_width

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, new_height: float) -> None:
        self._raise_exception_if_invalid_dimension(new_height)
        self._height = new_height

    def __eq__(self, other: Dimensions) -> bool:
        return (
            self.length == other.length and self.width == other.width
            and self.height == other.height
        )

    @staticmethod
    def _raise_exception_if_invalid_dimension(dimension: float) -> None:
        if dimension < 0:
            raise ValueError("Cannot have negative dimensions.")
