from src.main.freight.consignment.address import Address
from src.main.forward_office.dashboard.parser.requests.types \
    import AddressParseRequest

from src.main.forward_office.dashboard.parser.model.address.validation \
    import AddressValidationStrategy


class AddressParser:
    def __init__(self):
        self._validation = AddressValidationStrategy()

    def parse(self, request: AddressParseRequest) -> Address:
        errors = self._validation.validate(request)

        if errors:
            raise ValueError(errors)

        return self._parse(request)

    @staticmethod
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

