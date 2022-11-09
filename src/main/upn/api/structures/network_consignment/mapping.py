import dataclasses
from src.main.file_system.upn.api import structures as file_structures
from src.main.upn.api.structures.mapping.mapping import mapping_fields


NetworkConsignmentStructure = dataclasses.make_dataclass(
    cls_name="NetworkConsignmentStructure",
    fields=mapping_fields(file_structures.network_consignment())
)
