import copy
from src.main.freight.cargo.model import Cargo
from src.main.freight.cargo.entries.entry import CargoEntry
from src.main.forward_office.mapping.cargo import FclCargoTypeMap
from src.main.freight.cargo.entries import validation
from src.main.freight.cargo.entries.validation import CargoErrors

from src.main.forward_office.consignment_import.parser.requests.types \
    import CargoParseRequest, CargoEntryParseRequest


class CargoParseException(ValueError):
    def __init__(self, message, errors: CargoErrors):
        super().__init__(message)
        self.errors = errors


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
        errors = find_errors(request)
        self._process(errors) if errors else self._process(request)

    def _process(
            self, request: CargoEntryParseRequest or CargoErrors) -> None:
        request_type_handlers = {
            CargoEntryParseRequest: self._process_cargo_entry,
            CargoErrors: self._process_error
        }

        if type(request) in request_type_handlers:
            handle = request_type_handlers[type(request)]
            handle(request)

        else:
            raise TypeError("Invalid type.")

    @staticmethod
    def _process_error(errors) -> None:
        if errors.are_critical():
            raise CargoParseException(
                message=("Cargo parse errors", errors), errors=errors)

    def _process_cargo_entry(self, request: CargoEntryParseRequest) -> None:
        package_type = getattr(self._mappings, request.package_type)

        new_entry = CargoEntry(package_type)
        new_entry.quantity = int(request.quantity)
        new_entry.weight_kgs = float(request.weight)

        self._cargo.add(new_entry)


def find_errors(request: CargoEntryParseRequest) -> CargoErrors:
    validator = validation.CargoValidationStrategy()
    errors = CargoErrors()

    errors.invalid_package_type = not validator.validate_package_type(
        request.package_type)

    errors.blank_package_type = not validator.validate_package_type(
        request.package_type)

    errors.weight_incorrect = not validator.validate_weight(request.weight)
    errors.invalid_quantity = not validator.validate_quantity(request.quantity)
    errors.blank_line = errors.blank_package_type and errors.weight_incorrect

    return errors

