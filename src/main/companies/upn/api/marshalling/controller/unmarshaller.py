from src.main.companies.upn.api.constraints import network_consignment


class UPNAPIUnmarshaller:
    def __init__(self):
        self._mapping = network_consignment.constraints()

    def unmarshall(self, candidate: dict[str, any], field_name: str) -> any:
        return candidate[self.map_interface_to(field_name)]

    def map_interface_to(self, field_name: str):
        return getattr(self._mapping, field_name).constraints
