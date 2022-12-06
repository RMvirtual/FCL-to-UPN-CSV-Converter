from src.main.companies.upn.api.data_types.containers.implementation \
    import UPNAPIContainers


class UPNContainersMarshaller:
    def __init__(self):
        self._containers = UPNAPIContainers()

    def unmarshall_to_type(self, type_name: str) -> type:
        return self._containers[type_name]

    def unmarshall_to_instance(self, type_name: str) -> any:
        return self._unmarshall_container(type_name)

    def __contains__(self, type_name: str) -> bool:
        return self.contains(type_name)

    def contains(self, type_name: str) -> bool:
        return type_name in self._containers

    def _unmarshall_container(self, type_name: str):
        return self._containers[type_name]()
