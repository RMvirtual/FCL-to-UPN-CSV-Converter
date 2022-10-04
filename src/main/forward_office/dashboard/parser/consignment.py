from src.main.freight.consignment.consignment import Consignment
from src.main.forward_office.dashboard.parser.address import AddressParser


class ConsignmentParser:
    def __init__(self, field_indexes: dict[str, int]):
        self._field_indexes = field_indexes

    def parse(self, dashboard_input: list[str]) -> Consignment:
        consignment = Consignment()

        consignment.address = AddressParser(self._field_indexes).parse(
            dashboard_input)

        return consignment
