from enum import Enum, auto
from src.main.freight.service.main.interface import MainServiceInterface


class MainService(MainServiceInterface):
    class Options(Enum):
        economy = auto()
        next_day = auto()

    def __init__(self):
        self._option = self.Options.economy

    def economy(self) -> None:
        self._option = self.Options.economy

    def next_day(self) -> None:
        self._option = self.Options.next_day

    def is_economy(self) -> bool:
        return self._option == self.Options.economy

    def is_next_day(self) -> bool:
        return self._option == self.Options.next_day
