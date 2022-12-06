from src.main.file_system.companies.upn import api
from src.main.companies.upn.interfaces.services.service import UPNService
from src.main.companies.upn.implementations.services.specific.service \
    import UPNService as UPNServiceImpl


class UPNServicesDatabase:
    def __init__(self):
        self._data_file = api.network_consignment()

    def main_service(self) -> UPNService:
        return self._service_from_data_file("main_service")

    def premium_service(self) -> UPNService:
        return self._service_from_data_file("premium_service")

    def tail_lift_required(self) -> UPNService:
        return self._service_from_data_file("tail_lift_required")

    def additional_service(self) -> UPNService:
        return self._service_from_data_file("additional_service")

    def _service_from_data_file(self, service_name: str) -> UPNService:
        values = self._data_file[service_name]
        constraints = values["values"]

        return UPNServiceImpl(constraints)