from __future__ import annotations
from src.main.consignment.cargo.types import *


class CargoEntry:
    def __init__(self, package_type: Pallet):
        self._package_type: Pallet = package_type
        self._no_of_packages: int = 0
        self._weight_kgs: float = 0

    def __iadd__(self, other_entry: CargoEntry) -> None:
        if self == other_entry:
            self._add_cargo_details(other_entry)

        else:
            raise ValueError("Incorrect pallet dimensions to combine.")

    def __eq__(self, other_entry: CargoEntry) -> bool:
        return self._package_type == other_entry.package_type

    def _add_cargo_details(self, other_entry: CargoEntry) -> None:
        self._no_of_packages += other_entry.quantity
        self._weight_kgs += other_entry.weight_kgs

    @property
    def package_type(self) -> Pallet:
        return self._package_type

    @package_type.setter
    def package_type(self, pallet_type: Pallet):
        self._package_type = pallet_type

    @property
    def quantity(self) -> int:
        return self._no_of_packages

    @quantity.setter
    def quantity(self, quantity: int) -> None:
        self._no_of_packages = quantity

    @property
    def weight_kgs(self) -> float:
        return self._weight_kgs

    @weight_kgs.setter
    def weight_kgs(self, weight: float) -> None:
        if weight / self._no_of_packages > self._package_type.max_weight_kgs:
            raise ValueError(
                "Desired weight too heavy for the current number of packages.")

        else:
            self._weight_kgs = weight

