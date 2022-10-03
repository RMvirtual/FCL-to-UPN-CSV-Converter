import copy
from src.main.freight.consignment.consignment import Cargo
from src.main.freight.cargo.entry import CargoEntry
from src.main.forward_office.cargo.type_mappings import FclCargoTypeMap
from src.main.forward_office.dashboard.parser.cargo import validation
from src.main.forward_office.dashboard.parser.cargo.validation \
    import CargoParseRequest, CargoParseErrors


class CargoParser:
    def __init__(self, field_indexes: dict[str, int]):
        self._fields = field_indexes
        self._cargo = Cargo()
        self._mappings = FclCargoTypeMap()

    @property
    def cargo(self) -> Cargo:
        return copy.copy(self._cargo)

    def parse(self, values: list[str]) -> None:
        self._cargo.clear()

        for request in self._requests_from_dashboard_input(values):
            self._process_request(request)

    def _process_request(self, request: CargoParseRequest):
        errors = validation.find_errors(request)
        self._process(errors) if errors else self._process(request)

    def _process(self, request: CargoParseRequest or CargoParseErrors) -> None:
        request_type_handlers = {
            CargoParseRequest: self._process_cargo_entry,
            CargoParseErrors: self._process_error
        }

        if type(request) in request_type_handlers:
            handle = request_type_handlers[type(request)]
            handle(request)

        else:
            raise TypeError("Invalid type.")

    @staticmethod
    def _process_error(errors):
        if errors.are_critical():
            raise validation.CargoParseException(
                message="Cargo parse errors", errors=errors)

    def _requests_from_dashboard_input(self, values: list[str]):
        return [
            self._request_by_line(number, values) for number in range(1, 5)]

    def _request_by_line(self, line_number: int, values: list[str]):
        result = validation.CargoParseRequest()

        result.short_code = values[self._field(line_number, "package_type")]
        result.quantity = values[self._field(line_number, "quantity")]
        result.weight = values[self._field(line_number, "weight")]

        return result

    def _field(self, line_number: int, name: str) -> int:
        full_field = "line_" + str(line_number) + "_" + name

        return self._fields[full_field]

    def _process_cargo_entry(self, request: validation.CargoParseRequest):
        package_type = getattr(self._mappings, request.short_code)

        new_entry = CargoEntry(package_type)
        new_entry.quantity = int(request.quantity)
        new_entry.weight_kgs = float(request.weight)

        self._cargo.add(new_entry)
