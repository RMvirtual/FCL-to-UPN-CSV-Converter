import copy
from dataclasses import dataclass
from src.main.freight.consignment.consignment import Cargo
from src.main.freight.cargo.entry import CargoEntry
from src.main.forward_office.cargo.type_mappings import FclCargoTypeMap


# noinspection PyClassHasNoInit
@dataclass
class CargoParseErrors:
    blank_package_type: bool = False
    weight_incorrect: bool = False
    invalid_quantity = False

    def __bool__(self):
        return (
            self.blank_package_type
            or self.weight_incorrect
            or self.invalid_quantity
        )

    def __len__(self):
        return (
            self.blank_package_type
            + self.weight_incorrect
            + self.invalid_quantity
        )


class CargoParser:
    def __init__(self, field_indexes: dict[str, int]):
        self._fields = field_indexes
        self._cargo = Cargo()
        self._mappings = FclCargoTypeMap()
        self._errors = CargoParseErrors()

    def parse(self, values: list[str]) -> None:
        self._cargo.clear()
        self._validate_cargo_line("line_1", values)

        if not self._errors:
            self._parse_cargo_line("line_1", values)

        else:
            raise ValueError(self.errors)

    @property
    def cargo(self) -> Cargo:
        return copy.copy(self._cargo)

    @property
    def errors(self) -> CargoParseErrors:
        return copy.copy(self._errors)

    def _validate_cargo_line(self, line_number, values):
        short_code = values[self._fields[line_number + "_package_type"]]

        if not short_code:
            self._errors.blank_package_type = True

        quantity = int(values[self._fields[line_number + "_quantity"]])

        if quantity == 0:
            self._errors.invalid_quantity = True

        weight = float(values[self._fields[line_number + "_weight"]])

        if weight == 0:
            self._errors.weight_incorrect = True

    def _parse_cargo_line(self, line_number: str, values):
        short_code = values[self._fields[line_number + "_package_type"]]
        self._parse_with_short_code(short_code, line_number, values)

    def _parse_with_short_code(self, short_code, line_number, values):
        package_type = getattr(self._mappings, short_code)
        new_entry = CargoEntry(package_type)

        quantity = int(values[self._fields[line_number + "_quantity"]])
        new_entry.quantity = quantity

        weight = float(values[self._fields[line_number + "_weight"]])
        new_entry.weight_kgs = weight

        self._cargo.add(new_entry)

    def _extract_value(self, csv_row: list[str], field: str) -> str:
        field_column_index = self._fields[field]
        value = csv_row[field_column_index]

        return self._trim_whitespace(str(value))

    @staticmethod
    def _trim_whitespace(value: str):
        return " ".join(value.split())
