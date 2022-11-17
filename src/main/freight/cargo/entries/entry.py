from __future__ import annotations
from src.main.freight.cargo.packages.types.package_types import PackageType
import copy


class CargoEntry:
    def __init__(self, package_type: PackageType):
        self.package_type = copy.copy(package_type)
        self._quantity: int = 0
        self._weight: float = 0

    def __iadd__(self, other: CargoEntry) -> CargoEntry:
        if self == other:
            self._add_cargo_details(other)

        else:
            raise ValueError("Incorrect pallet dimensions to combine.")

        return self

    def __eq__(self, other_entry: CargoEntry) -> bool:
        return self._package_type == other_entry.package_type

    def _add_cargo_details(self, other_entry: CargoEntry) -> None:
        self._quantity += other_entry.quantity
        self._weight += other_entry.weight_kgs

    @property
    def package_type(self) -> PackageType:
        return self._package_type

    @package_type.setter
    def package_type(self, package_type: PackageType):
        self._package_type = copy.deepcopy(package_type)

    @property
    def quantity(self) -> int:
        return self._quantity

    @quantity.setter
    def quantity(self, new_quantity: int) -> None:
        if self._can_amend_quantity(new_quantity):
            self._quantity = new_quantity

        else:
            raise ValueError(
                "Desired number of packages will cause average weight to "
                "exceed maximum."
            )

    @property
    def weight_kgs(self) -> float:
        return self._weight

    @weight_kgs.setter
    def weight_kgs(self, new_weight: float) -> None:
        if self._can_amend_weight(new_weight):
            self._weight = new_weight

        else:
            raise ValueError(
                "Desired weight of", new_weight, " will exceed average "
                "maximum of", self.package_type.maximum_weight, " spread "
                "across", self._quantity, " packages."
            )

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
        return weight > self._package_type.maximum_weight
