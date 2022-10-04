from src.main.freight.consignment.consignment import Consignment, Reference
from src.main.forward_office.dashboard.parser.address import AddressParser


class ConsignmentParser:
    def __init__(self, field_indexes: dict[str, int]):
        self._field_indexes = field_indexes

    def parse(self, dashboard_input: list[str]) -> Consignment:
        consignment = Consignment()

        consignment.address = AddressParser(self._field_indexes).parse(
            dashboard_input)

        consignment.reference = self._parse_reference(dashboard_input)

        return consignment

    def _parse_reference(self, dashboard_input: list[str]) -> Reference:
        dashboard_reference = dashboard_input[self._field_indexes["reference"]]
        
        return Reference(dashboard_reference)
