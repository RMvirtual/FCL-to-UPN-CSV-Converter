import dataclasses
from src.main.companies.upn.interfaces.services.container \
    import UPNServices as UPNServicesProvider

from src.main.companies.upn.interfaces.services.service import UPNService


@dataclasses.dataclass
class ServicesDetails:
    main: UPNService = None
    premium: UPNService = None
    tail_lift: UPNService = None
    additional: UPNService = None


class UPNServices(UPNServicesProvider):
    def __init__(self, services_details: ServicesDetails) -> None:
        self._main = services_details.main
        self._premium = services_details.premium
        self._tail_lift = services_details.tail_lift
        self._additional = services_details.additional

    @property
    def main_service(self) -> UPNService:
        return self._main

    @property
    def premium_service(self) -> UPNService:
        return self._premium

    @property
    def tail_lift_required(self) -> UPNService:
        return self._tail_lift

    @property
    def additional_service(self) -> UPNService:
        return self._additional
