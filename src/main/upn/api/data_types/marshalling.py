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
        self._validate_data_type_exists(type_name)

        return self._type(type_name)

    def unmarshall_to_instance(self, type_name: str, value: any = None) -> any:
        self._validate_data_type_exists(type_name)

        if self.is_primitive(type_name):
            return self._unmarshall_primitive(type_name, value)

        return self._unmarshall_container(type_name, value)

    def _unmarshall_primitive(self, type_name: str, value: any = None) -> any:
        unmarshall_type = self._primitives[type_name]

        return unmarshall_type(value) if value else unmarshall_type()

    def _unmarshall_container(self, type_name: str, value: any = None):
        return self._containers[type_name]()

    def _type(self, type_name: str) -> type:
        type_container = (
            self._primitives if self.is_primitive(type_name)
            else self._containers
        )

        return type_container[type_name]

    def _validate_data_type_exists(self, type_name):
        if not self.is_data_type(type_name):
            self._raise_invalid_type_error(type_name)

    def is_data_type(self, type_name: str) -> bool:
        return self.is_primitive(type_name) or self.is_container(type_name)

    def is_primitive(self, type_name: str) -> bool:
        return type_name in self._primitives

    def is_container(self, type_name: str) -> bool:
        return type_name in self._containers

    def _raise_invalid_type_error(self, type_name: str):
        raise ValueError("Type", type_name, "is invalid UPN data type.")
