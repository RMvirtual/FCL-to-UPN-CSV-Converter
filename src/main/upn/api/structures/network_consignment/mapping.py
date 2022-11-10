import dataclasses
from src.main.file_system.upn.api import structures as file_structures
from src.main.upn.api.structures.data_types.marshalling import map_fields


NetworkConsignmentStructure = dataclasses.make_dataclass(
    cls_name="NetworkConsignmentStructure",
    fields=map_fields(file_structures.network_consignment())
)
