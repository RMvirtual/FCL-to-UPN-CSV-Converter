from src.main.companies.upn.api.mapping import network_consignment
from src.main.companies.upn.implementations.references.references \
    import UPNReferences
from src.main.companies.upn.interfaces.references import ReferencesDownload

UPNDict = dict[str, any]


def unmarshall_references(candidate: UPNDict) -> ReferencesDownload:
    return UPNReferences(
        barcode=_unmarshall(candidate, "barcode"),
        consignment_no=_unmarshall(candidate, "consignment_no"),
        customer_ref=_unmarshall(candidate, "customer_reference")
    )


def _unmarshall(candidate: UPNDict, field_name: str) -> any:
    return candidate[_map_interface_to(field_name)]


def _map_interface_to(field_name: str):
    mapping = network_consignment.mapping()
    return getattr(mapping, field_name).mapping
