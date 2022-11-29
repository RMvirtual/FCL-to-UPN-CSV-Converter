from src.main.time.dates.interface.integer import IntegerDateInterface


class IntegerDate(IntegerDateInterface):
    def __init__(self, day: int, month: int, year: int) -> None:
        self._day = day
        self._month = month
        self._year = year

    @property
    def day(self) -> int:
        return self._day

    @property
    def month(self) -> int:
        return self._month

    @property
    def year(self) -> int:
        return self._year
