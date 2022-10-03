import copy
from src.main.freight.consignment.consignment import Cargo
from src.main.freight.cargo.entry import CargoEntry
from src.main.forward_office.cargo.type_mappings import FclCargoTypeMap
from src.main.forward_office.dashboard.parser.cargo import validation


class CargoParser:
    def __init__(self, field_indexes: dict[str, int]):
        self._fields = field_indexes
        self._cargo = Cargo()
        self._mappings = FclCargoTypeMap()

    @property
    def cargo(self) -> Cargo:
        return copy.copy(self._cargo)

    def parse(self, values: list[str]) -> None:
        self._cargo.clear()

        for line_number in ["line_1", "line_2", "line_3", "line_4"]:
            short_code = values[self._fields[line_number + "_package_type"]]
            quantity = values[self._fields[line_number + "_quantity"]]
            weight = values[self._fields[line_number + "_weight"]]

            errors = validation.find_errors(short_code, quantity, weight)

            if errors:
                self._handle_critical_error(errors)

            else:
                self._parse_cargo_line(short_code, quantity, weight)

    @staticmethod
    def _handle_critical_error(errors: validation.CargoParseErrors):
        if errors.blank_line:
            ...

        else:
            raise validation.CargoParseException(
                message="Cargo parse errors", errors=errors)

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
