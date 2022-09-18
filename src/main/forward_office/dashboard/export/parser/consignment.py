from src.main.freight.consignment.consignment import Consignment
from src.main.forward_office.dashboard.export.parser.address \
    import AddressParser


class ConsignmentParser:
    """
    Interprets a 2D list of strings into a consignment.
    The interpretation of the field heading for each list column
    is defined by the format parameter in the constructor.
    """
    def __init__(self, file_format: dict[str, int]):
        self._consignments: dict[str, Consignment] = {}
        self._format = file_format
        self._address_parser = AddressParser(self._format)

    def parse(self, csv_rows: list[list[str]]) -> dict[str, Consignment]:
        self._consignments.clear()

        for row in csv_rows:
            self._parse(row)

        return self._consignments

    def _parse(self, csv_row: list[str]) -> None:
        reference = csv_row[self._format["reference"]]

        if reference in self._consignments:
            self._append_consignment(csv_row)

        else:
            self._new_consignment(csv_row)

    def _append_consignment(self, csv_row: list[str]) -> None:
        pass

    def _new_consignment(self, csv_row: list[str]) -> None:
        consignment = self._parse_consignment(csv_row)
        self._consignments[consignment.reference] = consignment

    def _parse_consignment(self, csv_row: list[str]):
        consignment = Consignment()
        consignment.reference = self._extract_value(csv_row, "reference")
        consignment.address = self._address_parser.parse(csv_row)

        return consignment

    def _extract_value(self, csv_row, field: str) -> str:
        field_column_index = self._format[field]
        value = csv_row[field_column_index]

        return self._trim_whitespace(str(value))

    @staticmethod
    def _trim_whitespace(value: str):
        return " ".join(value.split())
