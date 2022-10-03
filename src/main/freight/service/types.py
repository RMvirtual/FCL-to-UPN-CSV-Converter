from enum import Enum


class MainService(Enum):
    PRIORITY = 1
    ECONOMY = 2


class PremiumService(Enum):
    AM = 1
    PRE_10AM = 2
    TIMED = 3
    SATURDAY_AM = 4


class BookedService(Enum):
    BOOK_IN = 1
    BOOKED = 2
