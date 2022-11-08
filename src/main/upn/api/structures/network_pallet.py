import dataclasses
from src.main.upn.api.structures.mapping import NetworkPalletStructure


def network_pallet_fields():
    structure = NetworkPalletStructure()
    field_names = dataclasses.fields(structure)

    for field in field_names:
        name = field.name
        mapping_values = getattr(structure, name)
        field_type = mapping_values.type


NetworkPallet = dataclasses.make_dataclass(
    cls_name="NetworkPallet",
    fields=network_pallet_fields()
)
