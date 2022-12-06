from src.main.companies.upn.implementations.services.container import (
    ServicesDetails, UPNServices)
from src.main.companies.upn.implementations.services.specific import UPNService
from src.main.companies.upn.interfaces.services.container \
    import ServicesProvider
from src.main.companies.upn.interfaces.services.specific import ServiceProvider
from src.main.file_system.companies.upn import api


class UPNServicesDatabase:
    """Factory for loading service types from UPN system configuration."""
    def __init__(self):
        self._data_file = api.network_consignment()

    def all_services(self) -> ServicesProvider:
        fields = ServicesDetails()
        fields.main = self.main_service()
        fields.premium = self.premium_service()
        fields.tail_lift = self.tail_lift_required()
        fields.additional = self.additional_service()

        return UPNServices(fields)

    def main_service(self) -> ServiceProvider:
        return self._service_from_data_file("main_service")

    def premium_service(self) -> ServiceProvider:
        return self._service_from_data_file("premium_service")

    def tail_lift_required(self) -> ServiceProvider:
        return self._service_from_data_file("tail_lift_required")

    def additional_service(self) -> ServiceProvider:
        return self._service_from_data_file("additional_service")

    def _service_from_data_file(self, service_name: str) -> ServiceProvider:
        values = self._data_file[service_name]
        constraints = values["values"]

        return UPNService(constraints)
