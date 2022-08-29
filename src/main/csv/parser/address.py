from src.main.json.fcl_format import FclConsignmentFormat
from src.main.consignment.address import Address


class AddressParser:
    def __init__(self, file_format: FclConsignmentFormat):
        self._format = file_format

    def parse(self, csv_row) -> Address:
        address = Address()

        address.name = self._extract_value(csv_row, "company_name")
        address.line_1 = self._extract_value(csv_row, "address_line_1")
        address.line_2 = self._extract_value(csv_row, "address_line_2")
        address.line_3 = self._extract_value(csv_row, "address_line_3")
        address.town = self._extract_value(csv_row, "town")
        address.post_code = self._extract_value(csv_row, "post_code")
        address.country = "GB"
        address.contact_name = self._extract_value(csv_row, "contact_name")
        address.telephone_number = self._extract_value(csv_row, "telephone_no")

        return address

    def _extract_value(self, csv_row, field: str) -> str:
        field_column_index = self._format[field]
        value = csv_row[field_column_index]

        return self._trim_whitespace(str(value))

    @staticmethod
    def _trim_whitespace(value: str):
        return " ".join(value.split())
