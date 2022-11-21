from __future__ import annotations
import copy
from src.main.graylaw.cargo.packages.types.interface import PackageType
from src.main.graylaw.cargo.entries import interface

from src.main.graylaw.cargo.entries.validation \
    import CargoEntryValidationStrategy


class CargoEntry(interface.CargoEntry):
    def __init__(self, package: PackageType, quantity: int, weight: float):
        self._package_type = copy.deepcopy(package)
        self._quantity = quantity
        self._weight = weight
        self._validation = CargoEntryValidationStrategy(entry_to_validate=self)

    @property
    def package_type(self) -> PackageType:
        return self._package_type

    @property
    def quantity(self) -> int:
        return self._quantity

    @quantity.setter
    def quantity(self, new_quantity: int) -> None:
        if not self._validation.is_quantity_valid(new_quantity):
            raise ValueError(
                "Desired number of packages will exceed maximum average "
                "weight."
            )

        self._quantity = new_quantity

    @property
    def weight(self) -> float:
        return self._weight

    @weight.setter
    def weight(self, weight: float) -> None:
        if not self._validation.is_total_weight_valid(weight):
            raise ValueError(
                "Desired weight of", weight, " will exceed average "
                "maximum of", self.package_type.maximum_weight, " spread "
                "across", self._quantity, " packages."
            )

        self._weight = weight

    def set_totals(self, quantity: int, weight: float) -> None:
        if not self._validation.are_metrics_valid(quantity, weight):
            raise ValueError("Totals exceed average maximum weight.")

        self._quantity = quantity
        self._weight = weight

    def __eq__(self, other_entry: CargoEntry) -> bool:
        return self._package_type == other_entry.package_type

    def __iadd__(self, other: CargoEntry) -> CargoEntry:
        if not self == other:
            raise ValueError("Incorrect pallet types to combine.")

        self._append_cargo(other)

        return self

    def _append_cargo(self, other: interface.CargoEntry) -> None:
        self.set_totals(
            quantity=self.quantity + other.quantity,
            weight=self.weight + other.weight
        )
