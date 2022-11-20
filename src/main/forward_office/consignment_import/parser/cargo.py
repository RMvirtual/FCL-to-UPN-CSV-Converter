import copy
from src.main.freight.cargo.model import Cargo
from src.main.freight.cargo.entries.entry import CargoEntry
from src.main.forward_office.mapping.cargo import FclCargoTypeMap

from src.main.forward_office.consignment_import.parser.requests.types \
    import CargoParseRequest, CargoEntryParseRequest


class CargoParser:
    def __init__(self):
        self._cargo = Cargo()
        self._mappings = FclCargoTypeMap()

    def parse(self, request: CargoParseRequest) -> Cargo:
        self._cargo.clear()

        if not request.line_1.is_empty():
            self._process_request(request.line_1)

        if not request.line_2.is_empty():
            self._process_request(request.line_2)

        if not request.line_3.is_empty():
            self._process_request(request.line_3)

        if not request.line_4.is_empty():
            self._process_request(request.line_4)

        return copy.copy(self._cargo)

    def _process_request(self, request: CargoEntryParseRequest) -> None:
        package_type = getattr(self._mappings, request.package_type)

        self._cargo.add(CargoEntry(
            package=package_type, quantity=int(request.quantity),
            weight=float(request.weight)
        ))
