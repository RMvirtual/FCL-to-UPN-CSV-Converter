from src.main.companies.upn.api.mapping import network_consignment
from src.main.companies.upn.interfaces.address import UPNAddressable
from src.main.companies.upn.implementations.address.address import UPNAddress
UPNDict = dict[str, any]


def unmarshall(candidate: UPNDict) -> UPNAddressable:
    result = UPNAddress()
    result.name = _unmarshall(candidate, "delivery_name")
    result.line_1 = _unmarshall(candidate, "delivery_address_1")
    result.line_2 = _unmarshall(candidate, "delivery_address_2")
    result.town = _unmarshall(candidate, "delivery_town")
    result.county = _unmarshall(candidate, "delivery_county")
    result.post_code = _unmarshall(candidate, "delivery_post_code")
    result.country = _unmarshall(candidate, "delivery_country")
    result.contact_name = _unmarshall(candidate, "delivery_contact_name")
    result.telephone_no = _unmarshall(candidate, "delivery_telephone_no")

    return result


def _unmarshall(candidate: UPNDict, field_name: str) -> any:
    return candidate[_map_interface_to(field_name)]


def _map_interface_to(field_name: str):
    mapping = network_consignment.mapping()
    return getattr(mapping, field_name).mapping
