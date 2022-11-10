from src.main.upn.api.data_structures.mapping.structure import Mapping
from src.main.upn.api.data_types.marshalling import DataTypeMarshaller


class MappingMarshaller:
    def __init__(self):
        self._data_types = DataTypeMarshaller()

    def to_mapping_values(self, values: dict) -> Mapping:
        result = Mapping()

        result.type = self._data_types.unmarshall_to_type(values["type"])
        result.mapping = values["mapping"]
        result.values = values["values"] if "values" in values else []

        return result

    def map_fields(self, contents: dict[str, dict]):
        return map(self._json_entry_to_field_values, contents.items())

    def _json_entry_to_field_values(self, field) -> list[str, any, Mapping]:
        key, value = field

        return [key, Mapping, self.to_mapping_values(value)]
