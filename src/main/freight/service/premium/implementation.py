from enum import Enum, auto
from src.main.freight.service.premium.interface import PremiumServiceInterface


class PremiumService(PremiumServiceInterface):
    class Options(Enum):
        NONE = auto()
        AM = auto()
        PRE_10AM = auto()
        TIMED = auto()

    def __init__(self):
        ...

    def am(self) -> None:
        ...

    def pre_10am(self) -> None:
        ...

    def timed(self) -> None:
        ...

    def clear(self) -> None:
        ...

    def is_am(self) -> bool:
        ...

    def is_pre_10am(self) -> bool:
        ...

    def is_timed(self) -> bool:
        ...

    def is_not_required(self) -> bool:
        ...

    def __bool__(self) -> bool:
        ...

    def __eq__(self, other: PremiumServiceInterface):
        ...
