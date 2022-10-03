import copy
from dataclasses import dataclass, fields
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
    invalid_package_type: bool = False

    def __bool__(self):
        all_fields = fields(self)

        for field in all_fields:
            if getattr(self, field.name):
                return True

        return False

    def __len__(self):
        error_count = 0
        all_fields = fields(self)

        for field in all_fields:
            if getattr(self, field.name):
                error_count += 1

        return error_count

    def reset(self):
        self.blank_line = False
        self.blank_package_type = False
        self.invalid_quantity = False
        self.weight_incorrect = False


class CargoParseException(ValueError):
    def __init__(self, message, errors: CargoParseErrors):
        super().__init__(message)
        self.errors = errors


def find_errors(
        short_code: str, quantity: str or int, weight: str or float
) -> CargoParseErrors:
    errors = CargoParseErrors()

    errors.blank_package_type = not short_code
    errors.invalid_quantity = not quantity
    errors.weight_incorrect = not weight

    errors.blank_line = (
        errors.weight_incorrect and errors.invalid_quantity
        and errors.blank_package_type
    )

    errors.invalid_package_type = not hasattr(FclCargoTypeMap, short_code)

    return copy.copy(errors)
