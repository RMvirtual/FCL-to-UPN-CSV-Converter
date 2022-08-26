from __future__ import annotations
from enum import Enum


class OversizeOptions(Enum):
    NORMAL = 1
    OVERSIZE = 2
    DOUBLE = 2
    TRIPLE = 3


class Pallet:
    def __init__(self, max_weight_kgs: float):
        self._max_weight_kgs: float = max_weight_kgs
        self._oversize = OversizeOptions.NORMAL

    def __eq__(self, other: Pallet) -> bool:
        return self._is_equal(other)

    def _is_equal(self, other: Pallet) -> bool:
        return self._matches_class(other) and self._matches_oversize(other)

    def _matches_class(self, other: Pallet) -> bool:
        return self.__class__ == other.__class__

    def _matches_oversize(self, other: Pallet) -> bool:
        return self._oversize == other.oversize_option

    @property
    def max_weight_kgs(self) -> float:
        return self._max_weight_kgs

    @property
    def oversize_option(self):
        return self._oversize

    @oversize_option.setter
    def oversize_option(self, option: OversizeOptions):
        self._oversize = option

    def is_normal_size(self) -> bool:
        return self._oversize == OversizeOptions.NORMAL

    def is_oversize(self) -> bool:
        return self._oversize == OversizeOptions.OVERSIZE

    def is_double(self) -> bool:
        return self._oversize == OversizeOptions.DOUBLE

    def is_triple(self) -> bool:
        return self._oversize == OversizeOptions.TRIPLE


class FullPallet(Pallet):
    def __init__(self):
        super().__init__(1200)


class HalfPallet(Pallet):
    def __init__(self):
        super().__init__(600)


class QuarterPallet(Pallet):
    def __init__(self):
        super().__init__(300)


class MicroPallet(Pallet):
    def __init__(self):
        super().__init__(150)
