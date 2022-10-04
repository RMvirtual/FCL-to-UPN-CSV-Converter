import datetime
import calendar

from src.main.freight.consignment.consignment import Consignment, Reference
from src.main.forward_office.dashboard.parser.address import AddressParser
from src.main.forward_office.dashboard.parser.cargo.model import CargoParser
from src.main.forward_office.dashboard.parser.service.model \
    import ServiceParser


class ConsignmentParser:
    def __init__(self, field_indexes: dict[str, int]):
        self._field_indexes = field_indexes

    def parse(self, dashboard_input: list[str]) -> Consignment:
        consignment = Consignment()

        consignment.address = AddressParser(self._field_indexes).parse(
            dashboard_input)

        consignment.reference = self._parse_reference(dashboard_input)

        cargo_parser = CargoParser(self._field_indexes)
        cargo_parser.parse(dashboard_input)
        consignment.cargo = cargo_parser.cargo

        consignment.delivery_instructions = self._parse_delivery_instructions(
            dashboard_input)

        consignment.client_name = dashboard_input[
            self._field_indexes["principal_client"]]

        consignment.service = ServiceParser(
            self._field_indexes).parse(dashboard_input)

        consignment.delivery_date = self._parse_delivery_date(dashboard_input)
        consignment.delivery_time = self._parse_delivery_time(dashboard_input)

        return consignment

    def _parse_reference(self, dashboard_input: list[str]) -> Reference:
        dashboard_reference = dashboard_input[self._field_indexes["reference"]]

        return Reference(dashboard_reference)

    def _parse_delivery_instructions(
            self, dashboard_input: list[str]) -> list[str]:
        start = self._field_indexes["delivery_instruction_1"]
        end = self._field_indexes["delivery_instruction_2"] + 1

        instructions = dashboard_input[start:end]

        return list(filter(bool, instructions))

    def _parse_delivery_date(
            self, dashboard_input: list[str]) -> datetime.date:
        date_string = dashboard_input[self._field_indexes["delivery_date"]]
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

    def _parse_delivery_time(
            self, dashboard_input: list[str]) -> datetime.time:
        time_string = dashboard_input[self._field_indexes["booking_time"]]
        # h:mmpm
        new_time = datetime.datetime.strptime(time_string, "%I:%M%p")

        return new_time
