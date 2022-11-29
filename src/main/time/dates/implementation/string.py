from src.main.time.dates.interface.string import StringDateInterface


class StringDate(StringDateInterface):
    def __init__(self, day: str, month: str, year: str) -> None:
        self._day = day
        self._month = month
        self._year = year

    @property
    def day(self) -> str:
        return self._day

    @property
    def month(self) -> str:
        return self._month

    @property
    def year(self) -> str:
        return self._year

