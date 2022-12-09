import dataclasses
from src.main.companies.upn.api.interface_1.database.services.container import (
    ServicesProvider, ServiceProvider)


@dataclasses.dataclass
class ServicesDetails:
    main: ServiceProvider = None
    premium: ServiceProvider = None
    tail_lift: ServiceProvider = None
    additional: ServiceProvider = None


class UPNServices(ServicesProvider):
    def __init__(self, services_details: ServicesDetails) -> None:
        self._main = services_details.main
        self._premium = services_details.premium
        self._tail_lift = services_details.tail_lift
        self._additional = services_details.additional

    @property
    def main_service(self) -> ServiceProvider:
        return self._main

    @property
    def premium_service(self) -> ServiceProvider:
        return self._premium

    @property
    def tail_lift_required(self) -> ServiceProvider:
        return self._tail_lift

    @property
    def additional_service(self) -> ServiceProvider:
        return self._additional
