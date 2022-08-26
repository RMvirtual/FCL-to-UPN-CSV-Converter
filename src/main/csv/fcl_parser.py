from enum import IntEnum
from src.main.csv.reader import read as read_csv
from src.main.consignment.consignment import Consignment


def read(csv_path: str, ignore_headers: bool = False) \
        -> dict[str, Consignment]:
    csv_rows = read_csv(src_path=csv_path, ignore_headers=ignore_headers)
    fcl_format = FclCsvFormat()

    return fcl_format.parse(csv_rows)


class FclCsvFormat:
    """Interprets a list of strings as a UPNEDIIMP FCL CSV export."""

    class Column(IntEnum):
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

    def __init__(self):
        self._consignments: dict[str, Consignment] = {}

    def parse(self, csv_rows: list[list[str]]) -> dict[str, Consignment]:
        self._consignments.clear()

        for row in csv_rows:
            self._parse(row)

        return self._consignments

    def _parse(self, csv_row: list[str]) -> None:
        reference = csv_row[self.Column.REFERENCE]

        if reference in self._consignments:
            self._append_consignment(csv_row)

        else:
            self._new_consignment(csv_row)

    def _append_consignment(self, csv_row: list[str]) -> None:
        pass

    def _new_consignment(self, csv_row: list[str]) -> None:
        consignment = Consignment()
        consignment.reference = csv_row[self.Column.REFERENCE]

        consignment.address.name = csv_row[self.Column.COMPANY_NAME]
        consignment.address.line_1 = csv_row[self.Column.ADDRESS_LINE_1]
        consignment.address.line_2 = csv_row[self.Column.ADDRESS_LINE_2]
        consignment.address.line_3 = csv_row[self.Column.ADDRESS_LINE_3]
        consignment.address.town = csv_row[self.Column.TOWN]

        cleaned_post_code = " ".join(csv_row[self.Column.POST_CODE].split())
        consignment.address.post_code = cleaned_post_code

        consignment.address.country = "GB"
        consignment.address.contact_name = csv_row[self.Column.CONTACT_NAME]

        consignment.address.telephone_number = csv_row[
            self.Column.TELEPHONE_NO]

        self._consignments[consignment.reference] = consignment



