import dataclasses


@dataclasses.dataclass
class UPNAPIContainers:
    dictionary: type = dict
    array: type = list

    def contains(self, mapping_name: str):
        return hasattr(self, mapping_name)

    def __contains__(self, mapping_name: str):
        return self.contains(mapping_name)

    def get(self, mapping_name: str) -> type:
        return getattr(self, mapping_name)

    def __getitem__(self, mapping_name: str) -> type:
        return self.get(mapping_name)


class UPNContainersMarshaller:
    def __init__(self):
        self._containers = UPNAPIContainers()

    def unmarshall_to_type(self, type_name: str) -> type:
        self._raise_type_error_if_invalid(type_name)

        return self._containers[type_name]

    def unmarshall_to_instance(self, type_name: str) -> any:
        self._raise_type_error_if_invalid(type_name)

        return self._unmarshall_container(type_name)

    def __contains__(self, type_name: str) -> bool:
        return self.contains(type_name)

    def contains(self, type_name: str) -> bool:
        return type_name in self._containers

    def _unmarshall_container(self, type_name: str):
        return self._containers[type_name]()

    def _raise_type_error_if_invalid(self, type_name: str) -> None:
        if not self.contains(type_name):
            self._raise_invalid_type_error(type_name)

    def _raise_invalid_type_error(self, type_name: str):
        raise ValueError("Type", type_name, "is invalid UPN data type.")
