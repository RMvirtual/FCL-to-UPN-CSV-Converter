from src.main.freight.consignment.address import Address


class AddressParser:
    def __init__(self, fields_to_indexes: dict[str, int]):
        self._fields_to_indexes = fields_to_indexes

    def parse(self, values: list[str]) -> Address:
        address = Address()

        address.name = self._extract_value(values, "company_name")
        address.line_1 = self._extract_value(values, "address_line_1")
        address.line_2 = self._extract_value(values, "address_line_2")
        address.line_3 = self._extract_value(values, "address_line_3")
        address.town = self._extract_value(values, "town")
        address.post_code = self._extract_value(values, "post_code")
        address.country = "GB"
        address.contact_name = self._extract_value(values, "contact_name")
        address.telephone_number = self._extract_value(values, "telephone_no")

        return address

    def _extract_value(self, csv_row: list[str], field: str) -> str:
        field_column_index = self._fields_to_indexes[field]
        value = csv_row[field_column_index]

        return self._trim_whitespace(str(value))

    @staticmethod
    def _trim_whitespace(value: str):
        return " ".join(value.split())
