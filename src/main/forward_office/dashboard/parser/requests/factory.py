import datetime
import calendar

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

    def cargo_request(self, values: list[str]) -> CargoParseRequest:
        cleaned_values = list(map(self._trim_whitespace, values))

        return self._cargo_request(cleaned_values)

    def _cargo_request(self, values: list[str]) -> CargoParseRequest:
        cleaned_values = list(map(self._trim_whitespace, values))

        result = CargoParseRequest()

        result.line_1 = self.cargo_entry(1, cleaned_values)
        result.line_2 = self.cargo_entry(2, cleaned_values)
        result.line_3 = self.cargo_entry(3, cleaned_values)
        result.line_4 = self.cargo_entry(4, cleaned_values)

        return result

    def cargo_entry(
            self, line: int, values: list[str]) -> \
            CargoEntryParseRequest or None:
        cleaned_values = list(map(self._trim_whitespace, values))

        return self._cargo_entry(line, cleaned_values)

    def _cargo_entry(
            self, line: int, values: list[str]) -> CargoEntryParseRequest:
        result = CargoEntryParseRequest()

        result.package_type = values[self._line_string(line, "package_type")]
        result.quantity = values[self._line_string(line, "quantity")]
        result.weight = values[self._line_string(line, "weight")]
        result.goods_description = values[
            self._line_string(line, "description")]

        return result

    def _line_string(self, line_number: int, name: str) -> int:
        full_field = "line_" + str(line_number) + "_" + name

        return self._column_indexes[full_field]

    def reference_request(self, values: list[str]):
        cleaned_values = list(map(self._trim_whitespace, values))

        return cleaned_values[self._column_indexes["reference"]]

    def delivery_instructions(self, values: list[str]):
        cleaned_values = list(map(self._trim_whitespace, values))

        start = self._column_indexes["delivery_instruction_1"]
        end = self._column_indexes["delivery_instruction_2"] + 1

        instructions = cleaned_values[start:end]

        return list(filter(bool, instructions))

    def principal_client(self, values: list[str]):
        cleaned_values = list(map(self._trim_whitespace, values))

        return cleaned_values[self._column_indexes["principal_client"]]

    def delivery_date(self, values: list[str]):
        cleaned_values = list(map(self._trim_whitespace, values))
        date_string = cleaned_values[self._column_indexes["delivery_date"]]
        day, month, year = date_string.split("-")

        abbreviations = {
            month: index for index, month in enumerate(calendar.month_abbr)
            if month
        }

        return datetime.date(
            day=int(day),
            month=abbreviations[month],
            year=int("20" + year)
        )

    def delivery_time(self, values: list[str]):
        cleaned_values = list(map(self._trim_whitespace, values))

        time_string = cleaned_values[self._column_indexes["booking_time"]]
        # h:mmpm (fcl's time format).
        new_time = datetime.datetime.strptime(time_string, "%I:%M%p")

        return new_time

    @staticmethod
    def _trim_whitespace(value: str):
        return " ".join(value.split()) if value else value
