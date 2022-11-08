import dataclasses
from src.main.file_system.upn.api import structures
from src.main.upn.api.structures.mapping.mapping import _field_values


def network_consignment_fields():
    return _field_values(structures.network_consignment())


NetworkConsignmentStructure = dataclasses.make_dataclass(
    cls_name="NetworkConsignmentStructure",
    fields=network_consignment_fields()
)
