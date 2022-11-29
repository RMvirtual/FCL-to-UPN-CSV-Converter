import copy
from src.main.freight.cargo.entries.interface import CargoEntry
from src.main.freight.cargo.entries import validation
from src.main.freight.cargo.entries.validation import EntryValidationStrategy
from src.main.freight.cargo.packages.types.interface import PackageType


class CargoEntryModel(CargoEntry):
    def __init__(self, package: PackageType, quantity: int, weight: float):
        self._package_type = copy.deepcopy(package)
        self._quantity = quantity
        self._weight = weight
        self._validation = EntryValidationStrategy(entry_to_validate=self)

    @property
    def package_type(self) -> PackageType:
        return self._package_type

    @property
    def quantity(self) -> int:
        return self._quantity

    @quantity.setter
    def quantity(self, new_quantity: int) -> None:
        self._assert_quantity_is_valid(new_quantity)
        self._quantity = new_quantity

    @property
    def weight(self) -> float:
        return self._weight

    @weight.setter
    def weight(self, new_weight: float) -> None:
        self._assert_total_weight_is_valid(new_weight)
        self._weight = new_weight

    def set_totals(self, quantity: int, weight: float) -> None:
        self._assert_metrics_are_valid(quantity, weight)
        self._quantity = quantity
        self._weight = weight

    def __eq__(self, other_entry: CargoEntry) -> bool:
        return self._package_type == other_entry.package_type

    def __iadd__(self, other: CargoEntry) -> CargoEntry:
        self._assert_cargo_entry_matches(other)
        self._append_cargo(other)

        return self

    def _append_cargo(self, other: CargoEntry) -> None:
        self.set_totals(
            quantity=self.quantity + other.quantity,
            weight=self.weight + other.weight
        )

    def _assert_metrics_are_valid(self, quantity: int, weight: float) -> None:
        if not self._validation.are_metrics_valid(quantity, weight):
            raise validation.TotalsInvalid()

    def _assert_quantity_is_valid(self, new_quantity: int) -> None:
        if not self._validation.is_quantity_valid(new_quantity):
            raise validation.InvalidQuantity()

    def _assert_total_weight_is_valid(self, new_weight: float) -> None:
        if not self._validation.is_total_weight_valid(new_weight):
            raise validation.TotalWeightInvalid(
                weight=new_weight,
                max_weight_per_package=self.package_type.maximum_weight,
                quantity=self.quantity
            )

    def _assert_cargo_entry_matches(self, other: CargoEntry) -> None:
        if not self == other:
            raise validation.InvalidPackageTypes()
