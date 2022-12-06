import dataclasses
from src.main.file_system.companies.upn import api
from src.main.companies.upn.api.data_types.constraints import (
    Constraints, ConstraintsMarshaller)


@dataclasses.dataclass
class NetworkConsignmentConstraints:
    consignment_no: Constraints = None
    barcode: Constraints = None
    customer_reference: Constraints = None
    depot_no: Constraints = None
    customer_id: Constraints = None
    customer_name: Constraints = None
    despatch_date: Constraints = None
    delivery_datetime: Constraints = None
    delivery_name: Constraints = None
    delivery_address_1: Constraints = None
    delivery_address_2: Constraints = None
    delivery_town: Constraints = None
    delivery_county: Constraints = None
    delivery_post_code: Constraints = None
    delivery_telephone_no: Constraints = None
    delivery_contact_name: Constraints = None
    delivery_country: Constraints = None
    special_instructions: Constraints = None
    customer_paperwork_pages: Constraints = None
    main_service: Constraints = None
    premium_service: Constraints = None
    tail_lift_required: Constraints = None
    additional_service: Constraints = None
    pallets: Constraints = None
    total_weight: Constraints = None


def constraints() -> NetworkConsignmentConstraints:
    """Reliant on the network adaptors UPN JSON file having the same
    fields as the NetworkConsignmentInterface dataclass.
    """
    marshaller = ConstraintsMarshaller()
    constraints_file = api.network_consignment_constraints()
    result = NetworkConsignmentConstraints()

    for field in list(dataclasses.fields(NetworkConsignmentConstraints)):
        field_mapping = marshaller.unmarshal_constraint(
            constraints_file[field.name])
        setattr(result, field.name, field_mapping)

    return result
