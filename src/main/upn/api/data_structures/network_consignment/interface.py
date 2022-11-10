import dataclasses
from src.main.file_system.upn.api import structures

from src.main.upn.api.data_structures.mapping.marshalling import (
    Mapping, MappingMarshaller)


@dataclasses.dataclass
class NetworkConsignmentInterface:
    consignment_no: Mapping = None
    depot_no: Mapping = None
    customer_reference: Mapping = None
    despatch_date: Mapping = None
    delivery_name: Mapping = None
    delivery_address_1: Mapping = None
    delivery_address_2: Mapping = None
    delivery_town: Mapping = None
    delivery_county: Mapping = None
    delivery_post_code: Mapping = None
    delivery_telephone_no: Mapping = None
    total_weight: Mapping = None
    special_instructions: Mapping = None
    customer_id: Mapping = None
    customer_name: Mapping = None
    delivery_contact_name: Mapping = None
    delivery_country: Mapping = None
    customer_paperwork_pages: Mapping = None
    main_service: Mapping = None
    premium_service: Mapping = None
    tail_lift_required: Mapping = None
    additional_service: Mapping = None
    delivery_datetime: Mapping = None
    consignment_barcode_no: Mapping = None
    pallets: Mapping = None


def network_consignment() -> NetworkConsignmentInterface:
    """Reliant on the network consignment UPN JSON file having the same
    fields as the NetworkConsignmentInterface dataclass.
    """
    marshaller = MappingMarshaller()
    structure = structures.network_pallet()
    result = NetworkConsignmentInterface()

    for field in list(dataclasses.fields(NetworkConsignmentInterface)):
        mapping = marshaller.unmarshal_to_mapping(structure[field.name])
        setattr(result, field.name, mapping)

    return result
