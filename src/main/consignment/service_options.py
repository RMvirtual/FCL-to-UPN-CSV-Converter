from enum import Enum


class MainService:
    class Options(Enum):
        NEXT_DAY = 1
        ECONOMY = 2

    def __init__(self):
        self._option = MainService.Options.NEXT_DAY

    @property
    def option(self):
        return self._option

    def next_day(self) -> None:
        self._option = MainService.Options.NEXT_DAY

    def economy(self) -> None:
        self._option = MainService.Options.ECONOMY

    def is_next_day(self) -> bool:
        return self._option == MainService.Options.NEXT_DAY

    def is_economy(self) -> bool:
        return self._option == MainService.Options.ECONOMY


class PremiumService:
    class Options(Enum):
        AM = 1
        PRE_10AM = 2
        TIMED = 3
        SATURDAY_AM = 4

    def __init__(self):
        self._option = None

    @property
    def option(self):
        return self._option

    def not_required(self) -> None:
        self._option = None

    def am(self) -> None:
        self._option = PremiumService.Options.AM

    def pre_10am(self) -> None:
        self._option = PremiumService.Options.PRE_10AM

    def timed(self) -> None:
        self._option = PremiumService.Options.TIMED

    def saturday_am(self) -> None:
        self._option = PremiumService.Options.SATURDAY_AM

    def is_not_required(self) -> bool:
        return self._option is None

    def is_am(self) -> bool:
        return self._option == PremiumService.Options.AM

    def is_pre10am(self) -> bool:
        return self._option == PremiumService.Options.PRE_10AM

    def is_timed(self) -> bool:
        return self._option == PremiumService.Options.TIMED

    def is_saturday_am(self) -> bool:
        return self._option == PremiumService.Options.SATURDAY_AM


class AdditionalService:
    class Options(Enum):
        BOOK_IN = 1
        BOOKED = 2

    def __init__(self):
        self._option = None

    @property
    def option(self):
        return self._option

    def not_required(self) -> None:
        self._option = None

    def book_in(self) -> None:
        self._option = AdditionalService.Options.BOOK_IN

    def booked_in(self) -> None:
        self._option = AdditionalService.Options.BOOKED

    def is_not_required(self) -> bool:
        return self._option is None

    def is_book_in(self) -> bool:
        return self._option == AdditionalService.Options.BOOK_IN

    def is_booked_in(self) -> None:
        return self._option == AdditionalService.Options.BOOKED


class TailLiftService:
    def __init__(self):
        self._is_required = False

    def required(self) -> None:
        self._is_required = True

    def not_required(self) -> None:
        self._is_required = False

    def is_required(self) -> bool:
        return self._is_required

    def is_not_required(self) -> bool:
        return self._is_required is False


class ServiceOptions:
    def __init__(self):
        self._main_service = MainService()
        self._premium_service = PremiumService()
        self._additional_service = AdditionalService()
        self._tail_lift = TailLiftService()

    @property
    def main_service(self) -> MainService:
        return self._main_service

    @property
    def premium_service(self) -> PremiumService:
        return self._premium_service

    @property
    def additional_service(self) -> AdditionalService:
        return self._additional_service

    @property
    def tail_lift(self) -> TailLiftService:
        return self._tail_lift
