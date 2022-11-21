import dataclasses
from src.main.file_system.upn.api import structures

from src.main.upn.api.data_structures.mapping.marshalling import (
    Mapping, MappingMarshaller)


@dataclasses.dataclass
class NetworkConsignmentMapping:
    consignment_no: Mapping = None
    barcode: Mapping = None
    customer_reference: Mapping = None
    depot_no: Mapping = None
    customer_id: Mapping = None
    customer_name: Mapping = None
    despatch_date: Mapping = None
    delivery_datetime: Mapping = None
    delivery_name: Mapping = None
    delivery_address_1: Mapping = None
    delivery_address_2: Mapping = None
    delivery_town: Mapping = None
    delivery_county: Mapping = None
    delivery_post_code: Mapping = None
    delivery_telephone_no: Mapping = None
    delivery_contact_name: Mapping = None
    delivery_country: Mapping = None
    special_instructions: Mapping = None
    customer_paperwork_pages: Mapping = None
    main_service: Mapping = None
    premium_service: Mapping = None
    tail_lift_required: Mapping = None
    additional_service: Mapping = None
    pallets: Mapping = None
    total_weight: Mapping = None


def network_consignment() -> NetworkConsignmentMapping:
    """Reliant on the network consignment UPN JSON file having the same
    fields as the NetworkConsignmentInterface dataclass.
    """
    marshaller = MappingMarshaller()
    structure = structures.network_consignment()
    result = NetworkConsignmentMapping()

    for field in list(dataclasses.fields(NetworkConsignmentMapping)):
        mapping = marshaller.unmarshal_to_mapping(structure[field.name])
        setattr(result, field.name, mapping)

    return result
