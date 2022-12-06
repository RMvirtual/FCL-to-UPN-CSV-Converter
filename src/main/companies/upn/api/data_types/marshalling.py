from src.main.companies.upn.api.data_types.containers \
    import UPNContainersMarshaller

from src.main.companies.upn.api.data_types.primitives \
    import UPNPrimitiveMarshaller


class UPNDataTypeMarshaller:
    def __init__(self):
        self._primitives = UPNPrimitiveMarshaller()
        self._containers = UPNContainersMarshaller()

    def unmarshall_to_type(self, type_name: str) -> type:
        self._validate_data_type_exists(type_name)

        return self._type(type_name)

    def unmarshall_to_instance(self, type_name: str, value: any = None) -> any:
        self._validate_data_type_exists(type_name)

        return (
            self._unmarshall_primitive(type_name, value)
            if type_name in self._primitives
            else self._unmarshall_container(type_name)
        )

    def is_data_type(self, type_name: str) -> bool:
        return type_name in self._primitives or type_name in self._containers

    def _unmarshall_primitive(self, type_name: str, value: any = None) -> any:
        return self._primitives.unmarshall_to_instance(type_name, value)

    def _unmarshall_container(self, type_name: str):
        return self._containers.unmarshall_to_instance(type_name)

    def _type(self, type_name: str) -> type:
        type_container = (
            self._primitives if type_name in self._primitives
            else self._containers
        )

        return type_container.unmarshall_to_type(type_name)

    def _validate_data_type_exists(self, type_name):
        if not self.is_data_type(type_name):
            self._raise_invalid_type_error(type_name)

    def _raise_invalid_type_error(self, type_name: str):
        raise ValueError("Type", type_name, "is invalid UPN data type.")
