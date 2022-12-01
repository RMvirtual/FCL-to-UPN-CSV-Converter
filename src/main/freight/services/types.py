from enum import Enum
import dataclasses


class MainService(Enum):
    PRIORITY = 1
    ECONOMY = 2


class PremiumService(Enum):
    AM = 1
    PRE_10AM = 2
    TIMED = 3


class BookedService(Enum):
    BOOK_IN = 1
    BOOKED = 2


@dataclasses.dataclass
class ServiceOptions:
    main_service: MainService = MainService.PRIORITY
    premium_service: PremiumService or None = None
    booked_service: BookedService or None = None
    saturday: bool = False
