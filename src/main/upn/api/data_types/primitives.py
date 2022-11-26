import dataclasses
import datetime


@dataclasses.dataclass
class UPNAPIPrimitives:
    string: type = str
    int: type = int
    datetime: type = datetime.datetime

    def contains(self, mapping_name: str):
        return hasattr(self, mapping_name)

    def __contains__(self, mapping_name: str):
        return self.contains(mapping_name)

    def get(self, mapping_name: str) -> type:
        return getattr(self, mapping_name)

    def __getitem__(self, mapping_name: str) -> type:
        return self.get(mapping_name)


class UPNPrimitiveMarshaller:
    def __init__(self):
        self._primitives = UPNAPIPrimitives()

    def unmarshall_to_type(self, type_name: str) -> type:
        self._raise_type_error_if_invalid(type_name)

        return self._primitives[type_name]

    def unmarshall_to_instance(self, type_name: str, value: any = None) -> any:
        self._raise_type_error_if_invalid(type_name)

        return self._unmarshall_primitive(type_name, value)

    def contains(self, type_name: str) -> bool:
        return type_name in self._primitives

    def __contains__(self, type_name: str) -> bool:
        return self.contains(type_name)

    def _unmarshall_primitive(self, type_name: str, value: any = None) -> any:
        unmarshall_type = self._primitives[type_name]

        return unmarshall_type(value) if value else unmarshall_type()

    def _raise_type_error_if_invalid(self, type_name):
        if not self.contains(type_name):
            self._raise_invalid_type_error(type_name)

    def _raise_invalid_type_error(self, type_name: str):
        raise ValueError("Type", type_name, "is invalid UPN data type.")
