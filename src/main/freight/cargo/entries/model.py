import copy
from src.main.freight.cargo.entries.interface import CargoEntry
from src.main.freight.cargo.entries.validation import EntryValidationStrategy
from src.main.freight.cargo.packages.types.interface import PackageType


class CargoEntryModel(CargoEntry):
    def __init__(self, package: PackageType, quantity: int, weight: float):
        self._package_type = copy.deepcopy(package)
        self._quantity = quantity
        self._weight = weight
        self._validation = EntryValidationStrategy(self)

    @property
    def package_type(self) -> PackageType:
        return self._package_type

    @property
    def quantity(self) -> int:
        return self._quantity

    @quantity.setter
    def quantity(self, new_quantity: int) -> None:
        self._validation.assert_quantity_is_valid(new_quantity)
        self._quantity = new_quantity

    @property
    def weight(self) -> float:
        return self._weight

    @weight.setter
    def weight(self, new_weight: float) -> None:
        self._validation.assert_total_weight_is_valid(new_weight)
        self._weight = new_weight

    def set_totals(self, quantity: int, weight: float) -> None:
        self._validation.assert_metrics_are_valid(quantity, weight)
        self._quantity = quantity
        self._weight = weight

    def __eq__(self, other_entry: CargoEntry) -> bool:
        return self._package_type == other_entry.package_type

    def __iadd__(self, other: CargoEntry) -> CargoEntry:
        self._append_cargo(other)

        return self

    def _append_cargo(self, other: CargoEntry) -> None:
        self._validation.assert_cargo_entry_is_compatible(other)

        self.set_totals(
            quantity=self.quantity + other.quantity,
            weight=self.weight + other.weight
        )
