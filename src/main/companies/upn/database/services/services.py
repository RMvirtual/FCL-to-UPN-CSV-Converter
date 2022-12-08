from src.main.companies.upn.database.consignment.network.keys \
    import NetworkConsignmentKeys
from src.main.companies.upn.database.implementation.service.container \
    import ServicesDetails, UPNServices
from src.main.companies.upn.database.implementation.service.specific \
    import UPNService
from src.main.companies.upn.api.interface_1.database.services.container \
    import ServicesProvider
from src.main.companies.upn.api.interface_1.database.services.specific \
    import ServiceProvider
from src.main.file_system.companies.upn.api.consignments.network \
    import NetworkConsignmentFiles


class UPNServicesDatabase:
    """Factory for loading service types from UPN system configuration."""
    def __init__(self):
        self._upn_keys = NetworkConsignmentKeys()
        self._data = NetworkConsignmentFiles()

    def all_services(self) -> ServicesProvider:
        fields = ServicesDetails()
        fields.main = self.main_service()
        fields.premium = self.premium_service()
        fields.tail_lift = self.tail_lift_required()
        fields.additional = self.additional_service()

        return UPNServices(fields)

    def main_service(self) -> ServiceProvider:
        return self._service_from_data_file(self._upn_keys.main_service)

    def premium_service(self) -> ServiceProvider:
        return self._service_from_data_file(self._upn_keys.premium_service)

    def tail_lift_required(self) -> ServiceProvider:
        return self._service_from_data_file(self._upn_keys.tail_lift_required)

    def additional_service(self) -> ServiceProvider:
        return self._service_from_data_file(self._upn_keys.additional_service)

    def _service_from_data_file(self, service_name: str) -> ServiceProvider:
        values = self._data.constraints[service_name]
        constraints = values["values"]

        return UPNService(constraints)
