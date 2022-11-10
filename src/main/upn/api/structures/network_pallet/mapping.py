import dataclasses
from src.main.file_system.upn.api import structures
from src.main.upn.api.structures.data_types.marshalling import map_fields


NetworkPalletStructure = dataclasses.make_dataclass(
    cls_name="NetworkPalletStructure",
    fields=map_fields(structures.network_pallet()),
    namespace={
        "field": lambda self, field_name: getattr(self, field_name)
    }
)
