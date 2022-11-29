from src.main.freight.cargo.entries.interface import CargoEntry


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
