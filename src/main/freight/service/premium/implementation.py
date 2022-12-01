from enum import Enum, auto
from src.main.freight.service.premium.interface import PremiumServiceInterface


class PremiumService(PremiumServiceInterface):
    class Options(Enum):
        NONE = auto()
        AM = auto()
        PRE_10AM = auto()
        TIMED = auto()

    def __init__(self):
        self._selected = self.Options.NONE

    def am(self) -> None:
        self._selected = self.Options.AM

    def pre_10am(self) -> None:
        self._selected = self.Options.PRE_10AM

    def timed(self) -> None:
        self._selected = self.Options.TIMED

    def clear(self) -> None:
        self._selected = self.Options.NONE

    def is_am(self) -> bool:
        return self._selected == self.Options.AM

    def is_pre_10am(self) -> bool:
        return self._selected == self.Options.PRE_10AM

    def is_timed(self) -> bool:
        return self._selected == self.Options.TIMED

    def is_not_required(self) -> bool:
        return self._selected == self.Options.NONE

    def __bool__(self) -> bool:
        return self._selected != self.Options.NONE

    def __eq__(self, other: PremiumServiceInterface):
        callback_options = {
            self.Options.NONE: other.is_not_required,
            self.Options.AM: other.is_am,
            self.Options.PRE_10AM: other.is_pre_10am,
            self.Options.TIMED: other.is_timed
        }

        return callback_options[self._selected]()
