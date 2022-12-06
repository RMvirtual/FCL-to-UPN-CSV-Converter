from src.main.companies.upn.api.mapping import network_consignment
from src.main.companies.upn.implementations.customer import UPNCustomer
from src.main.companies.upn.interfaces.customer import CustomerDetails

UPNDict = dict[str, any]


def unmarshall(candidate: UPNDict) -> CustomerDetails:
    return UPNCustomer(
        customer_name=_unmarshall(candidate, "customer_name"),
        customer_id=_unmarshall(candidate, "customer_id")
    )


def _unmarshall(candidate: UPNDict, field_name: str) -> any:
    return candidate[_map_interface_to(field_name)]


def _map_interface_to(field_name: str):
    mapping = network_consignment.mapping()
    return getattr(mapping, field_name).mapping
