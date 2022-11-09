import dataclasses

from src.main.upn.api.structures.network_pallet.mapping \
    import NetworkPalletStructure

from src.main.upn.api.structures.primitives.base_types import UpnApiPrimitives


def network_pallet_fields():
    fields = NetworkPalletFields()

    return fields.from_dataclass(NetworkPalletStructure())


class NetworkPalletFields:
    def __init__(self):
        self._primitives = UpnApiPrimitives()

    def from_dataclass(self, structure: dataclasses.dataclass) -> list:
        field_names = dataclasses.fields(structure)

        return [
            self._field_from_structure(field, structure)
            for field in field_names
        ]

    def _field_from_structure(
            self, field: dataclasses.Field, structure: dataclasses.dataclass
    ) -> list:
        mapping_values = structure.field(field.name)
        field_type = self._primitives[mapping_values.type]

        return [field.name, field_type, field_type()]


NetworkPallet = dataclasses.make_dataclass(
    cls_name="NetworkPallet",
    fields=network_pallet_fields()
)
