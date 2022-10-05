from src.main.freight.address.model import Address

from src.main.forward_office.dashboard.parser.requests.types \
    import AddressParseRequest

from src.main.freight.address.validation import (
    AddressValidationStrategy, AddressErrors)


def parse(request: AddressParseRequest) -> Address:
    errors = validate(request)

    if errors:
        raise ValueError(errors)

    return _parse(request)


def validate(request: AddressParseRequest) -> AddressErrors:
    validation = AddressValidationStrategy()
    errors = AddressErrors()

    errors.name_is_blank = not request.name
    errors.line_1_is_blank = not request.line_1
    errors.town_is_blank = not request.town
    errors.post_code_is_blank = not request.post_code

    errors.post_code_is_invalid = validation.validate_post_code(
        request.post_code)

    return errors


def _parse(request: AddressParseRequest):
    address = Address()

    address.name = request.name
    address.line_1 = request.line_1
    address.line_2 = request.line_2
    address.line_3 = request.line_3
    address.town = request.town
    address.post_code = request.post_code
    address.country = request.country
    address.contact_name = request.contact_name
    address.telephone_number = request.telephone_number

    return address
