import dataclasses
from src.main.upn.api.data_types.primitives import UpnApiPrimitives
from src.main.upn.api.data_types.containers import UpnApiContainers

@dataclasses.dataclass
class Mapping:
    type: str = ""
    mapping: str = ""
    values: list = None


def map_fields(contents: dict[str, dict]):
    return map(_json_entry_to_field_values, contents.items())


def _json_entry_to_field_values(field) -> list[str, any, Mapping]:
    key, value = field

    return [key, Mapping, _to_mapping_values(value)]


def _to_mapping_values(values: dict[str, str or list[str]]) -> Mapping:
    result = Mapping()
    result.type = values["type"]
    result.mapping = values["mapping"]
    result.values = values["values"] if "values" in values else []

    return result


class DataTypeMarshaller:
    def __init__(self):
        self._primitives = UpnApiPrimitives()
        self._containers = UpnApiContainers()

    def unmarshall_to_type(self, type_name: str) -> type:
        if type_name in self._primitives:
            return self._primitives[type_name]

        if type_name in self._containers:
            return self._containers[type_name]

        raise ValueError("Type", type_name, "is invalid UPN data type.")

    def unmarshall_to_instance(self) -> any:
        return None
