import dataclasses
import datetime
from src.main.upn.api.structures.mapping import NetworkConsignmentStructure
from src.main.upn.api.structures.network_pallet import NetworkPallet
from src.main.upn.api.structures.primitives import UpnApiPrimitives
import re


def network_consignment_fields():
    structure = NetworkConsignmentStructure()
    field_names = dataclasses.fields(structure)

    pallet_fields = []

    for field in field_names:
        mapping_values = getattr(structure, field.name)
        field_type = get_field_type(mapping_values.type)
        new_field = create_field(field.name, field_type)

        pallet_fields.append(new_field)

    return pallet_fields


def get_field_type(mapping_type_name: str) -> type:
    if is_primitive(mapping_type_name):
        return get_primitive(mapping_type_name)

    elif is_data_structure(mapping_type_name):
        return get_data_structure(mapping_type_name)

    elif is_array(mapping_type_name):
        nested_type_name = extract_array_object_name(mapping_type_name)
        nested_type = get_field_type(nested_type_name)

        return list[nested_type]

    else:
        raise ValueError(
            "Mapping type of " + mapping_type_name + " not found.")


def is_array(mapping_name: str):
    return bool(re.match("array_of", mapping_name))


def get_data_structure(mapping_name: str):
    structures = {
        "network_pallet": NetworkPallet,
        "network_consignment": NetworkConsignment
    }

    return structures[mapping_name]


def is_data_structure(mapping_name: str):
    return mapping_name in ("network_pallet", "network_consignment")


def extract_array_object_name(mapping_name: str) -> str:
    return re.sub("array_of_", "", mapping_name)


def create_field(name, field_type):
    if field_type is list:
        field_instance = dataclasses.field(default_factory=list)

    elif field_type is datetime.datetime:
        field_instance = None

    else:
        field_instance = field_type()

    return [name, field_type, field_instance]


def get_primitive(mapping_name: str):
    primitives = UpnApiPrimitives()

    return getattr(primitives, mapping_name)


def is_primitive(mapping_name: str):
    primitives = UpnApiPrimitives()

    return hasattr(primitives, mapping_name)


NetworkConsignment = dataclasses.make_dataclass(
    cls_name="NetworkConsignment",
    fields=network_consignment_fields()
)
