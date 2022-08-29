from enum import IntEnum
from src.main.csv.reader import read as read_csv
from src.main.consignment.consignment import Consignment
from src.main.json.fcl_format import FclConsignmentFormat


def read(csv_path: str, file_format: FclConsignmentFormat,
         ignore_headers: bool = False) -> dict[str, Consignment]:
    csv_rows = read_csv(src_path=csv_path, ignore_headers=ignore_headers)
    fcl_format = FclCsvFormat(file_format)

    return fcl_format.parse(csv_rows)


class FclCsvFormat:
    """Interprets a list of strings as a UPNEDIIMP FCL CSV export."""

    def __init__(self, file_format: FclConsignmentFormat):
        self._consignments: dict[str, Consignment] = {}
        self._format = file_format

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
        consignment = Consignment()

        consignment.reference = FclCsvFormat._trim_and_extract_list_element(
            csv_row, self._format["reference"])

        consignment.address.name = FclCsvFormat._trim_and_extract_list_element(
            csv_row, self._format["company_name"])

        consignment.address.line_1 = (
            FclCsvFormat._trim_and_extract_list_element(
                csv_row, self._format["address_line_1"])
        )

        consignment.address.line_2 = (
            FclCsvFormat._trim_and_extract_list_element(
                csv_row, self._format["address_line_2"])
        )

        consignment.address.line_3 = (
            FclCsvFormat._trim_and_extract_list_element(
                csv_row, self._format["address_line_3"])
        )

        consignment.address.town = FclCsvFormat._trim_and_extract_list_element(
            csv_row, self._format["town"])

        consignment.address.post_code = (
            FclCsvFormat._trim_and_extract_list_element(
                csv_row, self._format["post_code"])
        )

        consignment.address.country = "GB"

        consignment.address.contact_name = (
            FclCsvFormat._trim_and_extract_list_element(
                csv_row, self._format["contact_name"])
        )

        consignment.address.telephone_number = (
            FclCsvFormat._trim_and_extract_list_element(
                csv_row, self._format["telephone_no"])
        )

        self._consignments[consignment.reference] = consignment

    @staticmethod
    def _trim_and_extract_list_element(
            list_at_hand: list[str], index: int) -> str:
        return FclCsvFormat._trim_whitespace(str(list_at_hand[index]))

    @staticmethod
    def _trim_whitespace(value: str):
        return " ".join(value.split())
