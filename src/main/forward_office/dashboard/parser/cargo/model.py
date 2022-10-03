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
            self._parse_line(line_number, values)

    def _parse_line(self, line_number, values):
        parse_request = self._parse_request(line_number, values)
        errors = validation.find_errors(parse_request)

        if errors:
            self._handle_critical_error(errors)

        else:
            self._parse_cargo_line(parse_request)

    def _parse_request(self, line_number, values):
        result = validation.CargoParseRequest()

        result.short_code = values[self._fields[line_number + "_package_type"]]
        result.quantity = values[self._fields[line_number + "_quantity"]]
        result.weight = values[self._fields[line_number + "_weight"]]

        return result

    @staticmethod
    def _handle_critical_error(errors: validation.CargoParseErrors):
        if errors.blank_line:
            ...

        else:
            raise validation.CargoParseException(
                message="Cargo parse errors", errors=errors)

    def _parse_cargo_line(self, request: validation.CargoParseRequest):
        package_type = getattr(self._mappings, request.short_code)

        new_entry = CargoEntry(package_type)
        new_entry.quantity = int(request.quantity)
        new_entry.weight_kgs = float(request.weight)

        self._cargo.add(new_entry)

    def _extract_value(self, csv_row: list[str], field: str) -> str:
        field_column_index = self._fields[field]
        value = csv_row[field_column_index]

        return self._trim_whitespace(str(value))

    @staticmethod
    def _trim_whitespace(value: str):
        return " ".join(value.split())
