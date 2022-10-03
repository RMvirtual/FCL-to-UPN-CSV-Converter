from src.main.freight.service.types import (
    MainService, PremiumService, BookedService, ServiceOptions)


class ServiceValidationStrategy:
    def __init__(self, service_options: ServiceOptions):
        self._service_options = service_options

    def can_have_booked_service(self) -> bool:
        return self._service_options.main_service is MainService.ECONOMY

