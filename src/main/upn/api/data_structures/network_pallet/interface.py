import dataclasses
from src.main.upn.api.data_structures.mapping.marshalling import (
    Mapping, MappingMarshaller)

from src.main.file_system.upn.api import structures


@dataclasses.dataclass
class NetworkPalletInterface:
    barcode_no: Mapping = None
    type: Mapping = None
    size: Mapping = None
    consignment_barcode: Mapping = None


def network_pallet() -> NetworkPalletInterface:
    marshaller = MappingMarshaller()
    structure = structures.network_pallet()
    result = NetworkPalletInterface()

    result.barcode_no = marshaller.unmarshal_to_mapping(
        structure["barcode_no"])

    result.type = marshaller.unmarshal_to_mapping(structure["type"])
    result.size = marshaller.unmarshal_to_mapping(structure["size"])

    result.consignment_barcode = marshaller.unmarshal_to_mapping(
        structure["consignment_barcode"])

    return result
