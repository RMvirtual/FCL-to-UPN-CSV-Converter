from src.main.companies.upn.api.mapping import network_consignment
from src.main.companies.upn.interfaces.services.container \
    import ServicesProvider

from src.main.companies.upn.database.services import UPNServicesDatabase

UPNDict = dict[str, any]


def unmarshall(candidate: UPNDict) -> ServicesProvider:
    result = UPNServicesDatabase().all_services()
    result.main = _unmarshall(candidate, "main_service")
    result.premium = _unmarshall(candidate, "premium_service")
    result.tail_lift = _unmarshall(candidate, "tail_lift_required")
    result.additional = _unmarshall(candidate, "additional_service")

    return result


def _unmarshall(candidate: UPNDict, field_name: str) -> any:
    return candidate[_map_interface_to(field_name)]


def _map_interface_to(field_name: str):
    mapping = network_consignment.mapping()
    return getattr(mapping, field_name).mapping
