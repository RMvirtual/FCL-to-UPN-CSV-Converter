import copy
from dataclasses import dataclass
from src.main.freight.consignment.consignment import Cargo
from src.main.freight.cargo.entry import CargoEntry
from src.main.forward_office.cargo.type_mappings import FclCargoTypeMap


# noinspection PyClassHasNoInit
@dataclass
class CargoParseErrors:
    blank_line: bool = False
    blank_package_type: bool = False
    weight_incorrect: bool = False
    invalid_quantity: bool = False

    def __bool__(self):
        return (
            self.blank_line
            or self.blank_package_type
            or self.weight_incorrect
            or self.invalid_quantity
        )

    def __len__(self):
        return (
            self.blank_line
            + self.blank_package_type
            + self.weight_incorrect
            + self.invalid_quantity
        )

    def reset(self):
        self.blank_line = False
        self.blank_package_type = False
        self.invalid_quantity = False
        self.weight_incorrect = False


class CargoParseException(ValueError):
    def __init__(self, message, errors: CargoParseErrors):
        super().__init__(message)
        self.errors = errors


class CargoEntryParseValidator:
    def __init__(self):
        self._errors = CargoParseErrors()

    def find_errors(
            self, short_code: str, quantity: str or int,
            weight: str or float) -> CargoParseErrors:
        self._errors.blank_package_type = not short_code
        self._errors.invalid_quantity = not quantity
        self._errors.weight_incorrect = not weight

        self._errors.blank_line = (
            self._errors.weight_incorrect and self._errors.invalid_quantity
            and self._errors.blank_package_type
        )

        return copy.copy(self._errors)
