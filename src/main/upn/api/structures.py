import dataclasses
from src.main.upn.api.mapping_structures import NetworkConsignmentStructure


def network_consignment_fields():
    structure = NetworkConsignmentStructure()
    field_names = dataclasses.fields(structure)

    for field in field_names:
        name = field.name
        print(getattr(structure, name))


@dataclasses.dataclass
class NetworkConsignment:
    foo: str = ""
