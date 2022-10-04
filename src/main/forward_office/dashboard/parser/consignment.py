from src.main.freight.consignment.consignment import Consignment, Reference
from src.main.forward_office.dashboard.parser.address import AddressParser
from src.main.forward_office.dashboard.parser.cargo.model import CargoParser


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
