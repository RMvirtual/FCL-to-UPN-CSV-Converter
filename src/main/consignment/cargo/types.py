from enum import Enum


class Pallet:
    class OversizeOptions(Enum):
        NORMAL = 1
        OVERSIZE = 2
        DOUBLE = 2
        TRIPLE = 3

    def __init__(self, max_weight_kgs: int):
        self._max_weight_kgs: int = max_weight_kgs
        self._oversize_option = Pallet.OversizeOptions.NORMAL

    @property
    def oversize_option(self):
        return self._oversize_option

    @oversize_option.setter
    def oversize_option(self, option: OversizeOptions):
        self._oversize_option = option

    def is_normal_size(self) -> bool:
        return self._oversize_option == self.OversizeOptions.NORMAL

    def is_oversize(self) -> bool:
        return self._oversize_option == self.OversizeOptions.OVERSIZE

    def is_double(self) -> bool:
        return self._oversize_option == self.OversizeOptions.DOUBLE

    def is_triple(self) -> bool:
        return self._oversize_option == self.OversizeOptions.TRIPLE


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
