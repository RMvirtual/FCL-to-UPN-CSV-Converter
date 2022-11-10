import dataclasses

from src.main.upn.api.data_structures.network_pallet.mapping \
    import NetworkPalletStructure

from src.main.upn.api.data_types.primitives import UpnApiPrimitives


def network_pallet_fields():
    fields = NetworkPalletFields()

    return fields.from_dataclass(NetworkPalletStructure())


class NetworkPalletFields:
    def __init__(self):
        self._primitives = UpnApiPrimitives()

    def from_dataclass(self, structure: dataclasses.dataclass) -> list:
        return list(map(
            lambda field: [field.name, field.type, field.instance],
            self.field_attributes_from_structure(structure)
        ))

    @dataclasses.dataclass
    class MappingAttributes:
        name = None
        type = None
        instance = None

    def field_attributes_from_structure(
            self, structure: dataclasses.dataclass) -> MappingAttributes:
        result = []

        for structure_field in dataclasses.fields(structure):
            mapping_values = structure.field(structure_field.name)

            result.append(
                self.mapping_attributes_from_field(
                    structure_field, mapping_values
                )
            )

        return result

    def mapping_attributes_from_field(self, structure_field, mapping_values):
        result = self.MappingAttributes()

        result.name = structure_field.name
        result.type = self._primitives[mapping_values.type]
        result.instance = result.type()

        return result


NetworkPallet = dataclasses.make_dataclass(
    cls_name="NetworkPallet",
    fields=network_pallet_fields()
)
