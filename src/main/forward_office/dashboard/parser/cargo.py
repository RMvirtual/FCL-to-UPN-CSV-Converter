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


class CargoEntryParser:
    def __init__(self):
        self._errors = CargoParseErrors()

    def validate(
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


class CargoParser:
    def __init__(self, field_indexes: dict[str, int]):
        self._fields = field_indexes
        self._cargo = Cargo()
        self._mappings = FclCargoTypeMap()
        self._errors = CargoParseErrors()
        self._should_skip_line = False

    @property
    def cargo(self) -> Cargo:
        return copy.copy(self._cargo)

    @property
    def errors(self) -> CargoParseErrors:
        return copy.copy(self._errors)

    def parse(self, values: list[str]) -> None:
        self._cargo.clear()

        for line_number in ["line_1", "line_2", "line_3", "line_4"]:
            short_code = values[self._fields[line_number + "_package_type"]]
            quantity = values[self._fields[line_number + "_quantity"]]
            weight = values[self._fields[line_number + "_weight"]]

            validator = CargoEntryParser()
            self._errors = validator.validate(short_code, quantity, weight)

            if not self._errors:
                self._parse_cargo_line(short_code, quantity, weight)

            elif self._errors.blank_line:
                ...

            else:
                raise ValueError(self._errors)

    def _can_parse_cargo_line(self) -> bool:
        return not self._errors and not self._should_skip_line

    def _parse_cargo_line(self, short_code, quantity, weight):
        package_type = getattr(self._mappings, short_code)

        new_entry = CargoEntry(package_type)
        new_entry.quantity = int(quantity)
        new_entry.weight_kgs = float(weight)

        self._cargo.add(new_entry)

    def _extract_value(self, csv_row: list[str], field: str) -> str:
        field_column_index = self._fields[field]
        value = csv_row[field_column_index]

        return self._trim_whitespace(str(value))

    @staticmethod
    def _trim_whitespace(value: str):
        return " ".join(value.split())
