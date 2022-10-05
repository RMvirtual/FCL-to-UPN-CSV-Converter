from src.main.freight.consignment.consignment import Consignment

from src.main.forward_office.dashboard.parser.requests.types \
    import ConsignmentParseRequest

from src.main.forward_office.dashboard.parser.model.address.model \
    import AddressParser

from src.main.forward_office.dashboard.parser.model.cargo.model \
    import CargoParser

from src.main.forward_office.dashboard.parser.model.service.model \
    import ServiceParser


class ConsignmentParser:
    def __init__(self):
        pass

    def parse(self, request: ConsignmentParseRequest) -> Consignment:
        consignment = Consignment()

        consignment.client_name = request.principal_client
        consignment.reference = request.reference
        consignment.cargo = CargoParser().parse(request.cargo)
        consignment.delivery_instructions = request.delivery_instructions
        consignment.delivery_date = request.delivery_date
        consignment.delivery_time = request.delivery_time
        consignment.address = AddressParser().parse(request.address)
        consignment.service = ServiceParser().parse(request.service)

        return consignment
