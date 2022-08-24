from src.main.consignment.cargo.types import *


class CargoEntry:
    def __init__(self):
        self._pallet_type = None
        self._number_of_pallets = 0
        self._total_weight = 0

    @property
    def pallet_type(self) -> Pallet:
        return self._pallet_type

    @pallet_type.setter
    def pallet_type(self, pallet_type: Pallet):
        self._pallet_type = pallet_type

    @property
    def number_of_pallets(self) -> int:
        return self._number_of_pallets

    @number_of_pallets.setter
    def number_of_pallets(self, quantity: int) -> None:
        self._number_of_pallets = quantity

    @property
    def total_weight(self) -> int:
        return self._total_weight

    @total_weight.setter
    def total_weight(self, weight) -> None:
        self._total_weight = weight

