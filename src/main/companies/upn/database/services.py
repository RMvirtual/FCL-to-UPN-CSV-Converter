from src.main.companies.upn.implementations.services.container import (
    ServicesDetails, UPNServices)

from src.main.companies.upn.implementations.services.specific import UPNService
from src.main.companies.upn.interfaces.services.container import (
    ServicesProvider, ServiceProvider)

from src.main.file_system.companies.upn import api


class UPNServicesDatabase:
    """Factory for loading service types from UPN system configuration."""
    def __init__(self):
        self._key_mappings = api.network_consignment_keys()
        self._values = api.network_consignment_values()

    def all_services(self) -> ServicesProvider:
        fields = ServicesDetails()
        fields.main = self.main_service()
        fields.premium = self.premium_service()
        fields.tail_lift = self.tail_lift_required()
        fields.additional = self.additional_service()

        return UPNServices(fields)

    def main_service(self) -> ServiceProvider:
        upn_key = self._key_mappings["main_service"]

        return self._service_from_data_file(upn_key)

    def premium_service(self) -> ServiceProvider:
        upn_key = self._key_mappings["premium_service"]

        return self._service_from_data_file(upn_key)

    def tail_lift_required(self) -> ServiceProvider:
        upn_key = self._key_mappings["tail_lift_required"]

        return self._service_from_data_file(upn_key)

    def additional_service(self) -> ServiceProvider:
        upn_key = self._key_mappings["additional_service"]

        return self._service_from_data_file(upn_key)

    def _service_from_data_file(self, service_name: str) -> ServiceProvider:
        values = self._values[service_name]
        constraints = values["values"]

        return UPNService(constraints)
