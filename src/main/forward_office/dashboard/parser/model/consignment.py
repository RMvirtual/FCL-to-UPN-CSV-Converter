from src.main.freight.consignment.consignment import Consignment, Reference

from src.main.forward_office.dashboard.parser.model.address.model \
    import AddressParser

from src.main.forward_office.dashboard.parser.model.cargo.model \
    import CargoParser

from src.main.forward_office.dashboard.parser.model.service.model \
    import ServiceParser

from src.main.forward_office.dashboard.parser.requests.factory \
    import ParseRequestFactory


class ConsignmentParser:
    def __init__(self, field_indexes: dict[str, int]):
        self._field_indexes = field_indexes
        self._requests = ParseRequestFactory(self._field_indexes)

    def parse(self, dashboard_input: list[str]) -> Consignment:
        consignment = Consignment()

        address_request = self._requests.address_request(dashboard_input)
        consignment.address = AddressParser().parse(address_request)

        reference_request = self._requests.reference_request(dashboard_input)
        consignment.reference = Reference(reference_request)

        cargo_parser = CargoParser()
        cargo_request = self._requests.cargo_request(dashboard_input)
        consignment.cargo = cargo_parser.parse(cargo_request)

        consignment.delivery_instructions = (
            self._requests.delivery_instructions(dashboard_input))

        consignment.client_name = self._requests.principal_client(
            dashboard_input)

        consignment.service = ServiceParser(
            self._field_indexes).parse(dashboard_input)

        consignment.delivery_date = self._requests.delivery_date(
            dashboard_input)

        consignment.delivery_time = self._requests.delivery_time(
            dashboard_input)

        return consignment

