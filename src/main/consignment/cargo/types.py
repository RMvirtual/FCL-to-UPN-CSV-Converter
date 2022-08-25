from __future__ import annotations
from enum import Enum


class Pallet:
    class OversizeOptions(Enum):
        NORMAL = 1
        OVERSIZE = 2
        DOUBLE = 2
        TRIPLE = 3

    def __init__(self, max_weight_kgs: float):
        self._max_weight_kgs: float = max_weight_kgs
        self._oversize = Pallet.OversizeOptions.NORMAL

    def __eq__(self, other: Pallet) -> bool:
        return (
            self._pallet_class_matches(other)
            and self._oversize_option_matches(other)
        )

    def _pallet_class_matches(self, other: Pallet) -> bool:
        return self.__class__ == other.__class__

    def _oversize_option_matches(self, other: Pallet) -> bool:
        return self._oversize == other.oversize_option

    @property
    def oversize_option(self):
        return self._oversize

    @oversize_option.setter
    def oversize_option(self, option: OversizeOptions):
        self._oversize = option

    def is_normal_size(self) -> bool:
        return self._oversize == self.OversizeOptions.NORMAL

    def is_oversize(self) -> bool:
        return self._oversize == self.OversizeOptions.OVERSIZE

    def is_double(self) -> bool:
        return self._oversize == self.OversizeOptions.DOUBLE

    def is_triple(self) -> bool:
        return self._oversize == self.OversizeOptions.TRIPLE


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
