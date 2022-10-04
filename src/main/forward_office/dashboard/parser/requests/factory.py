from src.main.forward_office.dashboard.parser.requests.types import (
    AddressParseRequest, ServiceParseRequest, CargoEntryParseRequest,
    CargoParseRequest
)

from src.main.forward_office.dashboard.format.all import DashboardFormats


class ParseRequestFactory:
    def __init__(self, parsing_format: dict[str, int]):
        self._parsing_format = parsing_format

    def address_request(
            self, values_to_parse: list[str]) -> AddressParseRequest:
        result = AddressParseRequest()



        return result



    @staticmethod
    def _trim_whitespace(value: str):
        return " ".join(value.split())
