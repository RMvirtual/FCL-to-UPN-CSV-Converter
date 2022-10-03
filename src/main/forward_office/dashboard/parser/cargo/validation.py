import copy
import dataclasses
from src.main.forward_office.cargo.type_mappings import FclCargoTypeMap


# noinspection PyClassHasNoInit
@dataclasses.dataclass
class CargoParseErrors:
    blank_line: bool = False
    blank_package_type: bool = False
    weight_incorrect: bool = False
    invalid_quantity: bool = False
    invalid_package_type: bool = False

    def __bool__(self):
        for field in self._fields():
            if getattr(self, field.name):
                return True

        return False

    def __len__(self):
        error_count = 0

        for field in self._fields():
            if getattr(self, field.name):
                error_count += 1

        return error_count

    def reset(self):
        for field in self._fields():
            setattr(self, field.name, False)

    def _fields(self):
        return dataclasses.fields(self)


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

    blank_line_values = (
        errors.weight_incorrect,
        errors.invalid_quantity,
        errors.blank_package_type
    )

    errors.blank_line = all(blank_line_values)
    errors.invalid_package_type = not hasattr(FclCargoTypeMap, short_code)

    return copy.copy(errors)
