from __future__ import annotations
from src.main.consignment.cargo.types import *


class CargoEntry:
    def __init__(self, package_type: Pallet):
        self._package_type: Pallet = package_type
        self._quantity: int = 0
        self._weight: float = 0

    def __iadd__(self, other_entry: CargoEntry) -> None:
        if self == other_entry:
            self._add_cargo_details(other_entry)

        else:
            raise ValueError("Incorrect pallet dimensions to combine.")

    def __eq__(self, other_entry: CargoEntry) -> bool:
        return self._package_type == other_entry.package_type

    def _add_cargo_details(self, other_entry: CargoEntry) -> None:
        self._quantity += other_entry.quantity
        self._weight += other_entry.weight_kgs

    @property
    def quantity_and_weight(self) -> tuple[int, float]:
        return self._quantity, self._weight

    @quantity_and_weight.setter
    def quantity_and_weight(self, qty_and_weight: tuple[int, float]) -> None:
        quantity, weight = qty_and_weight
        average_weight = self._average_weight(quantity, weight)

        if self._max_weight_exceeded(average_weight):
            raise ValueError("New average weight will exceed maximum.")

        self._quantity = quantity
        self._weight = weight

    @property
    def package_type(self) -> Pallet:
        return self._package_type

    @property
    def quantity(self) -> int:
        return self._quantity

    @property
    def weight_kgs(self) -> float:
        return self._weight

    @package_type.setter
    def package_type(self, pallet_type: Pallet):
        self._package_type = pallet_type

    @quantity.setter
    def quantity(self, new_quantity: int) -> None:
        if self._can_amend_quantity(new_quantity):
            self._quantity = new_quantity

        else:
            raise ValueError(
                "Desired number of packages will cause average weight to "
                "exceed maximum."
            )

    @weight_kgs.setter
    def weight_kgs(self, new_weight: float) -> None:
        if self._can_amend_weight(new_weight):
            self._weight = new_weight

        else:
            raise ValueError("Desired weight will exceed average maximum.")

    def _can_amend_quantity(self, new_quantity: int) -> bool:
        average_weight = self._average_weight(new_quantity, self._weight)

        return not self._max_weight_exceeded(average_weight)

    def _can_amend_weight(self, new_weight: float) -> bool:
        average_weight = self._average_weight(self._quantity, new_weight)

        return not self._max_weight_exceeded(average_weight)

    @staticmethod
    def _average_weight(total_packages: int, total_weight: float) -> float:
        return total_weight / total_packages if total_packages else 0

    def _max_weight_exceeded(self, weight: float) -> bool:
        return weight > self._package_type.max_weight_kgs
