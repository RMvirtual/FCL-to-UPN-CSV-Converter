from __future__ import annotations
from src.main.consignment.cargo.types import *


class CargoEntry:
    def __init__(self):
        self._pallet_type: Pallet or None = None
        self._number_of_pallets: int = 0
        self._total_weight: float = 0

    def __iadd__(self, other_entry: CargoEntry) -> None:
        if self == other_entry:
            self._add_cargo_details(other_entry)

        else:
            raise ValueError("Incorrect pallet dimensions to combine.")

    def __eq__(self, other_entry: CargoEntry) -> bool:
        return self._pallet_type == other_entry.pallet_type

    def _add_cargo_details(self, other_entry: CargoEntry) -> None:
        self._number_of_pallets += other_entry.number_of_pallets
        self._total_weight += other_entry.total_weight

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
    def total_weight(self) -> float:
        return self._total_weight

    @total_weight.setter
    def total_weight(self, weight) -> None:
        self._total_weight = weight

