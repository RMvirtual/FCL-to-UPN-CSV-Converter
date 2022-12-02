import copy
from src.main.companies.bridges.graylaw.graylaw.forward_office\
    .consignment_import.parser.requests.types import ServiceParseRequest

from src.main.companies.bridges.graylaw.graylaw.forward_office.mapping.service \
    import FclServiceCodeMap

from src.main.freight.service.container.interface import Services


class ServiceParser:
    def __init__(self):
        self._mappings = FclServiceCodeMap()

    def parse(self, request: ServiceParseRequest) -> Services:
        service = self._mappings[request.priority_code]
        tail_lift_req = request.tail_lift_requested

        service.tail_lift() if tail_lift_req else ...

        return copy.copy(service)
