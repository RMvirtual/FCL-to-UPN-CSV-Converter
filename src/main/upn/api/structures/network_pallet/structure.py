import dataclasses

from src.main.upn.api.structures.network_pallet.mapping \
    import NetworkPalletStructure

from src.main.upn.api.structures.primitives.base_types import UpnApiPrimitives


def network_pallet_fields():
    structure = NetworkPalletStructure()
    field_names = dataclasses.fields(structure)

    pallet_fields = []
    primitives = UpnApiPrimitives()

    for field in field_names:
        name = field.name

        mapping_values = getattr(structure, name)

        field_type = mapping_values.type
        field_type = getattr(primitives, field_type)

        field_value = field_type()

        pallet_fields.append([name, field_type, field_value])

    return pallet_fields


NetworkPallet = dataclasses.make_dataclass(
    cls_name="NetworkPallet",
    fields=network_pallet_fields()
)
