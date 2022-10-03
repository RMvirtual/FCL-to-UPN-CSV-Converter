from src.main.freight.service.types import (
    MainService, PremiumService, BookedService)


class ServiceValidationStrategy:
    def __init__(
            self, main_service: MainService,
            premium_service: PremiumService or None,
            booked_service: BookedService or None
    ):
        self._main_service = main_service
        self._premium_service = premium_service
        self._booked_service = booked_service

    def can_have_booked_service(self) -> bool:
        return self._main_service is MainService.ECONOMY

