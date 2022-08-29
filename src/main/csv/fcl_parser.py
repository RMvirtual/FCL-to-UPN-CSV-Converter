from enum import IntEnum
from src.main.csv.reader import read as read_csv
from src.main.consignment.consignment import Consignment


def read(csv_path: str, ignore_headers: bool = False) \
        -> dict[str, Consignment]:
    csv_rows = read_csv(src_path=csv_path, ignore_headers=ignore_headers)
    fcl_format = FclCsvFormat()

    return fcl_format.parse(csv_rows)


class FclExportColumns(IntEnum):
    CONTACT_NAME = 0
    COMPANY_NAME = 1
    ADDRESS_LINE_1 = 2
    ADDRESS_LINE_2 = 3
    ADDRESS_LINE_3 = 4
    TOWN = 5
    POST_CODE = 6
    REFERENCE = 7
    TELEPHONE_NO = 8
    LINE_1_WEIGHT = 9
    LINE_1_QUANTITY = 10
    LINE_1_PACKAGE_TYPE = 11
    LINE_1_DESCRIPTION = 12
    PRINCIPAL_CLIENT = 13
    LINE_2_WEIGHT = 14
    LINE_2_QUANTITY = 15
    LINE_2_PACKAGE_TYPE = 16
    LINE_2_DESCRIPTION = 17
    LINE_3_WEIGHT = 18
    LINE_3_QUANTITY = 19
    LINE_3_PACKAGE_TYPE = 20
    LINE_3_DESCRIPTION = 21
    LINE_4_WEIGHT = 22
    LINE_4_QUANTITY = 23
    LINE_4_PACKAGE_TYPE = 24
    LINE_4_DESCRIPTION = 25
    DELIVERY_INSTRUCTION_1 = 26
    DELIVERY_INSTRUCTION_2 = 27
    BOOKING_TIME = 28
    DELIVERY_DATE = 29
    SHIPPER_REFERENCE = 30
    TOTAL_PALLETS = 31
    PRIORITY_CODE = 32
    TAIL_LIFT_REQUIRED = 33


class FclCsvFormat:
    """Interprets a list of strings as a UPNEDIIMP FCL CSV export."""

    def __init__(self):
        self._consignments: dict[str, Consignment] = {}

    def parse(self, csv_rows: list[list[str]]) -> dict[str, Consignment]:
        self._consignments.clear()

        for row in csv_rows:
            self._parse(row)

        return self._consignments

    def _parse(self, csv_row: list[str]) -> None:
        reference = csv_row[FclExportColumns.REFERENCE]

        if reference in self._consignments:
            self._append_consignment(csv_row)

        else:
            self._new_consignment(csv_row)

    def _append_consignment(self, csv_row: list[str]) -> None:
        pass

    def _new_consignment(self, csv_row: list[str]) -> None:
        consignment = Consignment()

        consignment.reference = FclCsvFormat._trim_and_extract_list_element(
            csv_row, FclExportColumns.REFERENCE)

        consignment.address.name = FclCsvFormat._trim_and_extract_list_element(
            csv_row, FclExportColumns.COMPANY_NAME)

        consignment.address.line_1 = (
            FclCsvFormat._trim_and_extract_list_element(
                csv_row, FclExportColumns.ADDRESS_LINE_1)
        )

        consignment.address.line_2 = (
            FclCsvFormat._trim_and_extract_list_element(
                csv_row, FclExportColumns.ADDRESS_LINE_2)
        )

        consignment.address.line_3 = (
            FclCsvFormat._trim_and_extract_list_element(
                csv_row, FclExportColumns.ADDRESS_LINE_3)
        )

        consignment.address.town = FclCsvFormat._trim_and_extract_list_element(
            csv_row, FclExportColumns.TOWN)

        consignment.address.post_code = (
            FclCsvFormat._trim_and_extract_list_element(
                csv_row, FclExportColumns.POST_CODE)
        )

        consignment.address.country = "GB"

        consignment.address.contact_name = (
            FclCsvFormat._trim_and_extract_list_element(
                csv_row, FclExportColumns.CONTACT_NAME)
        )

        consignment.address.telephone_number = (
            FclCsvFormat._trim_and_extract_list_element(
                csv_row, FclExportColumns.TELEPHONE_NO)
        )

        self._consignments[consignment.reference] = consignment

    @staticmethod
    def _trim_and_extract_list_element(
            list_at_hand: list[str], index: int) -> str:
        return FclCsvFormat._trim_whitespace(str(list_at_hand[index]))

    @staticmethod
    def _trim_whitespace(value: str):
        return " ".join(value.split())
