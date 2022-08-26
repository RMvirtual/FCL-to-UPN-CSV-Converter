from __future__ import annotations
from src.main.consignment.cargo.types import *


class CargoEntry:
    def __init__(self, package_type: Pallet):
        self._package_type: Pallet = package_type
        self._quantity: int = 0
        self._weight_kgs: float = 0

    def __iadd__(self, other_entry: CargoEntry) -> None:
        if self == other_entry:
            self._add_cargo_details(other_entry)

        else:
            raise ValueError("Incorrect pallet dimensions to combine.")

    def __eq__(self, other_entry: CargoEntry) -> bool:
        return self._package_type == other_entry.package_type

    def _add_cargo_details(self, other_entry: CargoEntry) -> None:
        self._quantity += other_entry.quantity
        self._weight_kgs += other_entry.weight_kgs

    @property
    def package_type(self) -> Pallet:
        return self._package_type

    @property
    def quantity(self) -> int:
        return self._quantity

    @property
    def weight_kgs(self) -> float:
        return self._weight_kgs

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
            self._weight_kgs = new_weight

        else:
            raise ValueError("Desired weight will exceed average maximum.")

    def _can_amend_quantity(self, new_quantity: int):
        average_weight = self._average_weight(self._weight_kgs, new_quantity)

        return not self._new_weight_exceeds_max(average_weight)

    def _can_amend_weight(self, new_weight: float):
        average_weight = self._average_weight(new_weight, self._quantity)

        return not self._new_weight_exceeds_max(average_weight)

    @staticmethod
    def _average_weight(total_weight, total_packages):
        return total_weight / total_packages if total_packages else 0

    def _new_weight_exceeds_max(self, new_weight_per_package: float):
        return new_weight_per_package > self._package_type.max_weight_kgs
