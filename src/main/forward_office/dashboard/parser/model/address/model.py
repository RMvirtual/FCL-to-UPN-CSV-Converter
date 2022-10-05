from src.main.freight.consignment.address import Address
from src.main.forward_office.dashboard.parser.requests.types \
    import AddressParseRequest


class AddressParser:
    def __init__(self):
        ...

    def parse(self, request: AddressParseRequest) -> Address:
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

