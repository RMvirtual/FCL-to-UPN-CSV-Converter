from src.main.forward_office.consignment_import.parser.requests.types import (
    AddressParseRequest, ServiceParseRequest, CargoEntryParseRequest,
    CargoParseRequest, ConsignmentParseRequest, ShipmentDatesRequest
)


class ParseRequestFactory:
    def __init__(self, parsing_format: dict[str, int]):
        self._columns = parsing_format

    def consignment_request(self, values: list[str]):
        cleaned_values = list(map(self._trim_whitespace, values))
        request = ConsignmentParseRequest()

        request.cargo = self._cargo_request(cleaned_values)
        request.service = self._service_request(cleaned_values)
        request.address = self._address_request(cleaned_values)
        request.principal_client = self.principal_client(cleaned_values)
        request.reference = self.reference_request(cleaned_values)

        request.delivery_instructions = self.delivery_instructions(
            cleaned_values)

        request.shipment_dates = ShipmentDatesRequest()

        request.shipment_dates.delivery_date = self.delivery_date(
            cleaned_values)

        request.shipment_dates.delivery_time = self.delivery_time(
            cleaned_values)

        return request

    def address_request(self, values: list[str]) -> AddressParseRequest:
        cleaned_values = list(map(self._trim_whitespace, values))

        return self._address_request(cleaned_values)

    def _address_request(self, values: list[str]):
        result = AddressParseRequest()

        result.name = values[self._columns["company_name"]]
        result.line_1 = values[self._columns["address_line_1"]]
        result.line_2 = values[self._columns["address_line_2"]]
        result.line_3 = values[self._columns["address_line_3"]]
        result.town = values[self._columns["town"]]
        result.post_code = values[self._columns["post_code"]]
        result.contact_name = values[self._columns["contact_name"]]
        result.telephone_number = values[self._columns["telephone_no"]]

        return result

    def service_request(self, values: list[str]) -> ServiceParseRequest:
        cleaned_values = list(map(self._trim_whitespace, values))

        return self._service_request(cleaned_values)

    def _service_request(self, values: list[str]) -> ServiceParseRequest:
        result = ServiceParseRequest()

        result.priority_code = values[self._columns["priority_code"]]

        result.tail_lift_requested = values[
            self._columns["tail_lift_required"]].lower() == "yes"

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

        return self._columns[full_field]

    def reference_request(self, values: list[str]):
        cleaned_values = list(map(self._trim_whitespace, values))

        return cleaned_values[self._columns["reference"]]

    def delivery_instructions(self, values: list[str]):
        cleaned_values = list(map(self._trim_whitespace, values))

        start = self._columns["delivery_instruction_1"]
        end = self._columns["delivery_instruction_2"] + 1

        instructions = cleaned_values[start:end]

        return list(filter(bool, instructions))

    def principal_client(self, values: list[str]):
        cleaned_values = list(map(self._trim_whitespace, values))

        return cleaned_values[self._columns["principal_client"]]

    def delivery_date(self, values: list[str]) -> ShipmentDatesRequest:
        cleaned_values = list(map(self._trim_whitespace, values))

        return cleaned_values[self._columns["delivery_date"]]

    def delivery_time(self, values: list[str]):
        cleaned_values = list(map(self._trim_whitespace, values))

        return cleaned_values[self._columns["booking_time"]]

    @staticmethod
    def _trim_whitespace(value: str):
        return " ".join(value.split()) if value else value
