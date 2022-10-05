import copy
from src.main.forward_office.mapping.service import FclServiceCodeMap
from src.main.freight.service.model import Service


class ServiceParser:
    def __init__(self, field_indexes: dict[str, int]):
        self._fields = field_indexes
        self._mappings = FclServiceCodeMap()

    def parse(self, dashboard_input: list[str]) -> Service:
        service = self._mappings[
            dashboard_input[self._fields["priority_code"]]]

        tail_lift_req = dashboard_input[self._fields["tail_lift_required"]]
        service.tail_lift() if tail_lift_req else ...

        return copy.copy(service)

