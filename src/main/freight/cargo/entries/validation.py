from src.main.freight.cargo.entries.interface import CargoEntry
from src.main.freight.cargo.entries import exceptions


class EntryValidationStrategy:
    def __init__(self, entry_to_validate: CargoEntry):
        self._entry = entry_to_validate

    def are_metrics_valid(self, quantity: int, weight: float) -> bool:
        average_weight = self._average_weight(quantity, weight)

        return self.is_individual_weight_valid(average_weight)

    def is_quantity_valid(self, quantity: int) -> bool:
        return self.are_metrics_valid(quantity, self._entry.weight)

    def is_total_weight_valid(self, weight: float) -> bool:
        return self.are_metrics_valid(self._entry.quantity, weight)

    def is_individual_weight_valid(self, weight: float) -> bool:
        return weight <= self._entry.package_type.maximum_weight

    @staticmethod
    def _average_weight(quantity: int, weight: float) -> float:
        return weight / quantity if quantity else 0

    def assert_metrics_are_valid(self, quantity: int, weight: float) -> None:
        if not self.are_metrics_valid(quantity, weight):
            raise exceptions.TotalsInvalid()

    def assert_quantity_is_valid(self, new_quantity: int) -> None:
        if not self.is_quantity_valid(new_quantity):
            raise exceptions.QuantityInvalid()

    def assert_total_weight_is_valid(self, new_weight: float) -> None:
        if not self.is_total_weight_valid(new_weight):
            raise exceptions.TotalWeightInvalid(
                total_weight=new_weight,
                max_weight_per_package=self._entry.package_type.maximum_weight,
                total_quantity=self._entry.quantity
            )

    def assert_cargo_entry_is_compatible(self, other: CargoEntry) -> None:
        if not self._entry == other:
            raise exceptions.PackageTypesInvalid()
