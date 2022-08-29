from src.main.csv.reader import read as read_csv
from src.main.consignment.consignment import Consignment
from src.main.json.fcl_format import FclConsignmentFormat
from src.main.csv.parser.address import AddressParser


def read(csv_path: str, file_format: FclConsignmentFormat,
         ignore_headers: bool = False) -> dict[str, Consignment]:
    csv_rows = read_csv(src_path=csv_path, ignore_headers=ignore_headers)
    fcl_format = ConsignmentParser(file_format)

    return fcl_format.parse(csv_rows)


class ConsignmentParser:
    """
    Interprets a 2D list of strings into a set of consignments.
    The ordering of this list is defined by the format parameter to
    determine which rows to use for each field.
    """

    def __init__(self, file_format: FclConsignmentFormat):
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
