from src.main.freight.consignment.consignment import Cargo
from src.main.freight.cargo.entry import CargoEntry
from src.main.forward_office.dashboard.cargo_type_mappings \
    import FclCargoTypeMappings


class CargoParser:
    def __init__(self, field_indexes: dict[str, int]):
        self._fields = field_indexes
        self._cargo = Cargo()

    def parse(self, values: list[str]) -> Cargo:
        self._cargo.clear()

        mappings = FclCargoTypeMappings()

        if values[self._fields["line_1_package_type"]] != "":
            package_type = getattr(
                mappings, values[self._fields["line_1_package_type"]])

            new_entry = CargoEntry(package_type)
            new_entry.quantity = int(values[self._fields["line_1_quantity"]])
            new_entry.weight_kgs = float(values[self._fields["line_1_weight"]])
            self._cargo.add(new_entry)

        return self._cargo

    def _extract_value(self, csv_row: list[str], field: str) -> str:
        field_column_index = self._fields[field]
        value = csv_row[field_column_index]

        return self._trim_whitespace(str(value))

    @staticmethod
    def _trim_whitespace(value: str):
        return " ".join(value.split())
