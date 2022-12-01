from src.main.freight.consignment.implementation import Consignment

from src.main.companies.bridges.graylaw_forward_office\
    .consignment_import.parser.requests.types \
    import ConsignmentParseRequest

from src.main.companies.bridges.graylaw_forward_office\
    .consignment_import.parser import \
    address, dates
from src.main.companies.bridges.graylaw_forward_office\
    .consignment_import.parser.cargo import CargoParser
from src.main.companies.bridges.graylaw_forward_office\
    .consignment_import.parser.service \
    import ServiceParser


class ConsignmentParser:
    def __init__(self):
        pass

    def parse(self, request: ConsignmentParseRequest) -> Consignment:
        consignment = Consignment(request.reference)

        consignment.client_name = request.principal_client
        consignment.cargo = CargoParser().parse(request.cargo)
        consignment.delivery_instructions = request.delivery_instructions

        consignment.shipment_dates = dates.parse(
            request.shipment_dates.delivery_date)

        consignment.shipment_dates.delivery = (
            request.shipment_dates.delivery_time)

        consignment.address = address.parse(request.address)
        consignment.service = ServiceParser().parse(request.service)

        return consignment
