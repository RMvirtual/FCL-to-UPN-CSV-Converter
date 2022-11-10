import dataclasses
from src.main.upn.api.data_structures.mapping.marshalling import (
    Mapping, MappingMarshaller)

from src.main.file_system.upn.api import structures


@dataclasses.dataclass
class NetworkPalletInterface:
    barcode: Mapping = None
    type: Mapping = None
    size: Mapping = None
    consignment_barcode: Mapping = None


def network_pallet() -> NetworkPalletInterface:
    """Reliant on the network pallet UPN JSON file having the same
    fields as the NetworkPalletInterface dataclass.
    """
    marshaller = MappingMarshaller()
    structure = structures.network_pallet()
    result = NetworkPalletInterface()

    for field in list(dataclasses.fields(NetworkPalletInterface)):
        mapping = marshaller.unmarshal_to_mapping(structure[field.name])
        setattr(result, field.name, mapping)

    return result
