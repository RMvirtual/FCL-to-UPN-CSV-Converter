from src.main.freight.service.options.interface.main import MainService
from src.main.freight.service.options.interface.premium import PremiumService
from src.main.freight.service.options.interface.booked import BookedService
from src.main.freight.service.options.interface.tail_lift \
    import TailLiftService

from src.main.freight.service.container.interface import Services
from src.main.freight.service.options import factory


class ServiceOptions(Services):
    def __init__(self):
        self._main = factory.main_service()
        self._premium = factory.premium_service()
        self._booked = factory.booked_service()
        self._tail_lift = factory.tail_lift_service()

    def main(self) -> MainService:
        return self._main

    def premium(self) -> PremiumService:
        return self._premium

    def booked(self) -> BookedService:
        return self._booked

    def tail_lift(self) -> TailLiftService:
        return self._tail_lift

    def __eq__(self, other: Services):
        return (
            self._main == other.main()
            and self._premium == other.premium()
            and self._booked == other.booked()
            and self._tail_lift == other.tail_lift()
        )
