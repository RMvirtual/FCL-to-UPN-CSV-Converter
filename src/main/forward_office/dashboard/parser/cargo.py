from src.main.freight.consignment.consignment import Cargo
from src.main.freight.cargo.entry import CargoEntry
from src.main.forward_office.cargo.type_mappings \
    import FclCargoTypeMap


class CargoParser:
    def __init__(self, field_indexes: dict[str, int]):
        self._fields = field_indexes
        self._cargo = Cargo()
        self._mappings = FclCargoTypeMap()

    def parse(self, values: list[str]) -> Cargo:
        self._cargo.clear()
        self._parse_cargo_line("line_1", values)

        return self._cargo

    def _parse_cargo_line(self, line_number: str, values):
        short_code = values[self._fields[line_number + "_package_type"]]

        if short_code:
            package_type = getattr(self._mappings, short_code)

            new_entry = CargoEntry(package_type)

            new_entry.quantity = int(
                values[self._fields[line_number + "_quantity"]])

            new_entry.weight_kgs = float(
                values[self._fields[line_number + "_weight"]])

            self._cargo.add(new_entry)

    def _extract_value(self, csv_row: list[str], field: str) -> str:
        field_column_index = self._fields[field]
        value = csv_row[field_column_index]

        return self._trim_whitespace(str(value))

    @staticmethod
    def _trim_whitespace(value: str):
        return " ".join(value.split())
