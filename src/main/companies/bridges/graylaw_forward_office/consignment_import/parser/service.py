import copy

from src.main.companies.bridges.graylaw_forward_office.mapping\
    .service import FclServiceCodeMap
from src.main.freight.services.model import Service

from src.main.companies.bridges.graylaw_forward_office\
    .consignment_import.parser.requests.types \
    import ServiceParseRequest


class ServiceParser:
    def __init__(self):
        self._mappings = FclServiceCodeMap()

    def parse(self, request: ServiceParseRequest) -> Service:
        service = self._mappings[request.priority_code]
        tail_lift_req = request.tail_lift_requested

        service.tail_lift() if tail_lift_req else ...

        return copy.copy(service)
