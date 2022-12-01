from enum import Enum, auto
from src.main.freight.service.options.interface.main import MainService


class MainOption(MainService):
    class Options(Enum):
        ECONOMY = auto()
        NEXT_DAY = auto()

    def __init__(self):
        self._option = self.Options.ECONOMY

    def economy(self) -> None:
        self._option = self.Options.ECONOMY

    def next_day(self) -> None:
        self._option = self.Options.NEXT_DAY

    def is_economy(self) -> bool:
        return self._option == self.Options.ECONOMY

    def is_next_day(self) -> bool:
        return self._option == self.Options.NEXT_DAY
