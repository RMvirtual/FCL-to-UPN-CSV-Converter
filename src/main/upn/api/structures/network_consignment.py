import dataclasses
from src.main.upn.api.structures.mapping import NetworkConsignmentStructure


def network_consignment_fields():
    structure = NetworkConsignmentStructure()
    field_names = dataclasses.fields(structure)

    for field in field_names:
        name = field.name
        mapping_values = getattr(structure, name)
        field_type = mapping_values.type


@dataclasses.dataclass
class NetworkConsignment:
    foo: str = ""
