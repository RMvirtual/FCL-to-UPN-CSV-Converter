from src.main.forward_office.dashboard.parser.requests.types import (
    AddressParseRequest, ServiceParseRequest, CargoEntryParseRequest,
    CargoParseRequest
)

from src.main.forward_office.dashboard.format.all import DashboardFormats


class ParseRequestFactory:
    def __init__(self, parsing_format: dict[str, int]):
        self._column_indexes = parsing_format

    def address_request(self, values: list[str]) -> AddressParseRequest:
        cleaned_values = list(map(self._trim_whitespace, values))

        return self._address_request(cleaned_values)

    def _address_request(self, values: list[str]):
        result = AddressParseRequest()

        result.name = values[self._column_indexes["company_name"]]
        result.line_1 = values[self._column_indexes["address_line_1"]]
        result.line_2 = values[self._column_indexes["address_line_2"]]
        result.line_3 = values[self._column_indexes["address_line_3"]]
        result.town = values[self._column_indexes["town"]]
        result.post_code = values[self._column_indexes["post_code"]]
        result.contact_name = values[self._column_indexes["contact_name"]]
        result.telephone_number = values[self._column_indexes["telephone_no"]]

        return result

    @staticmethod
    def _trim_whitespace(value: str):
        return " ".join(value.split()) if value else value
