from src.main.companies.upn.api.mapping import network_consignment
from src.main.companies.upn.interfaces.dates import DatesProvider
from src.main.companies.upn.implementations.dates import UPNDates

UPNDict = dict[str, any]


def unmarshall(candidate: UPNDict) -> DatesProvider:
    return UPNDates(
        despatch=_unmarshall(candidate, "despatch_date"),
        delivery=_unmarshall(candidate, "delivery_datetime")
    )


def _unmarshall(candidate: UPNDict, field_name: str) -> any:
    return candidate[_map_interface_to(field_name)]


def _map_interface_to(field_name: str):
    mapping = network_consignment.mapping()
    return getattr(mapping, field_name).mapping
