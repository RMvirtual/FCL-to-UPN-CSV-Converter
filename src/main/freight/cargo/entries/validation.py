import dataclasses
from src.main.freight.cargo.entries.interface import CargoEntry


class CargoEntryValidationStrategy:
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


@dataclasses.dataclass
class CargoErrors:
    blank_line: bool = False
    blank_package_type: bool = False
    weight_incorrect: bool = False
    invalid_quantity: bool = False
    invalid_package_type: bool = False

    def __bool__(self):
        return any(self._error_values())

    def __len__(self):
        return sum(self._error_values())

    def reset(self):
        for error in self._error_types():
            setattr(self, error.name, False)

    def _error_types(self):
        return dataclasses.fields(self)

    def _error_values(self) -> tuple[bool]:
        return (getattr(self, error.name) for error in self._error_types())

    def are_critical(self) -> bool:
        return bool(self) and not self.blank_line

