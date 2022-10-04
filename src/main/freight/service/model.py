from src.main.freight.service.types import (
    MainService, PremiumService, BookedService, ServiceOptions)

from src.main.freight.service.validation import ServiceValidationStrategy


class Service:
    def __init__(self):
        self._options = ServiceOptions()
        self._tail_lift: bool = False
        self._validation = ServiceValidationStrategy(self._options)

    def priority(self) -> None:
        self._options.main_service = MainService.PRIORITY

    def economy(self) -> None:
        self._options.main_service = MainService.ECONOMY

    def am(self) -> None:
        self._options.premium_service = PremiumService.AM

    def pre_10am(self) -> None:
        self._options.premium_service = PremiumService.PRE_10AM

    def timed(self) -> None:
        self._options.premium_service = PremiumService.TIMED

    def saturday(self) -> None:
        self._options.saturday = True

    def clear_saturday(self) -> None:
        self._options.saturday = False

    def no_premium_service(self):
        self._options.premium_service = None

    def book_in(self) -> None:
        self._options.booked_service = BookedService.BOOK_IN

    def booked(self) -> None:
        self._options.booked_service = BookedService.BOOKED

    def no_booked_service(self) -> None:
        self._options.booked_service = None

    def tail_lift(self) -> None:
        self._tail_lift = True

    def no_tail_lift(self) -> None:
        self._tail_lift = False

    def is_priority(self) -> bool:
        return self._options.main_service is MainService.PRIORITY

    def is_economy(self) -> bool:
        return self._options.main_service is MainService.ECONOMY

    def has_premium_service(self) -> bool:
        if self._options.premium_service is None:
            return False

        else:
            return (
                self._options.premium_service in PremiumService
                or self.is_saturday()
            )

    def is_am(self) -> bool:
        return self._options.premium_service is PremiumService.AM

    def is_pre_10am(self) -> bool:
        return self._options.premium_service is PremiumService.PRE_10AM

    def is_timed(self) -> bool:
        return self._options.premium_service is PremiumService.TIMED

    def is_saturday(self) -> bool:
        return self._options.saturday

    def has_booked_service(self) -> bool:
        return self._options.booked_service is BookedService

    def is_book_in(self) -> bool:
        return self._options.booked_service is BookedService.BOOK_IN

    def is_booked(self) -> bool:
        return self._options.booked_service is BookedService.BOOKED

    def is_tail_lift_required(self) -> bool:
        return self._tail_lift
