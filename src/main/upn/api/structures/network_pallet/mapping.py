import dataclasses
from src.main.file_system.upn.api import structures
from src.main.upn.api.structures.mapping.mapping import _field_values


def network_pallet_fields():
    return _field_values(structures.network_pallet())


NetworkPalletStructure = dataclasses.make_dataclass(
    cls_name="NetworkPalletStructure",
    fields=network_pallet_fields()
)
