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


@dataclasses.dataclass
class CargoParseRequest:
    short_code: str = ""
    quantity: str or int = ""
    weight: str or float = ""


class CargoParseException(ValueError):
    def __init__(self, message, errors: CargoParseErrors):
        super().__init__(message)
        self.errors = errors


def find_errors(parse_request: CargoParseRequest) -> CargoParseErrors:
    errors = CargoParseErrors()

    errors.blank_package_type = not parse_request.short_code
    errors.invalid_quantity = not parse_request.quantity
    errors.weight_incorrect = not parse_request.weight

    blank_line_values = (
        errors.weight_incorrect,
        errors.invalid_quantity,
        errors.blank_package_type
    )

    errors.blank_line = all(blank_line_values)
    errors.invalid_package_type = not FclCargoTypeMap().contains(
        parse_request.short_code)

    return copy.copy(errors)
