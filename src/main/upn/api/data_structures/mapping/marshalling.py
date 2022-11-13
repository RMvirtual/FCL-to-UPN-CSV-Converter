from src.main.upn.api.data_structures.mapping.structure import Mapping
from src.main.upn.api.data_types.marshalling import DataTypeMarshaller


class MappingMarshaller:
    def __init__(self):
        self._data_types = DataTypeMarshaller()

    def unmarshal_to_mapping(self, candidate: dict) -> Mapping:
        result = Mapping()

        result.type = self._data_types.unmarshall_to_type(candidate["type"])
        result.mapping = candidate["mapping"]
        result.values = candidate["values"] if "values" in candidate else []

        return result

    def unmarshal_to_dataclass_fields(self, candidate: dict[str, dict]):
        return map(self._json_entry_to_field_values, candidate.items())

    def _json_entry_to_field_values(self, field) -> list[str, any, Mapping]:
        key, value = field

        return [key, Mapping, self.unmarshal_to_mapping(value)]