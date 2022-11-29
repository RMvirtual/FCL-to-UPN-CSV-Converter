import datetime
from src.main.time.dates.interface import interface
from src.main.time.dates.model.comparison \
    import ComparisonStrategy


class Date(interface.Date):
    def __init__(self, day: int, month: int, year: int):
        self._date = datetime.date(day=day, month=month, year=year)
        self._comparison = ComparisonStrategy(self)

    @property
    def day(self) -> int:
        return self._date.day

    @property
    def month(self) -> int:
        return self._date.month

    @property
    def year(self) -> int:
        return self._date.year

    def __sub__(self, other: interface.Date) -> int:
        return self._comparison.difference_in_days(other)

    def __eq__(self, other: interface.Date) -> bool:
        return self._comparison.is_equal_to(other)

    def __lt__(self, other: interface.Date) -> bool:
        return self._comparison.is_less_than(other)

    def __le__(self, other: interface.Date) -> bool:
        return self._comparison.is_less_than_equal_to(other)

    def __ge__(self, other: interface.Date) -> bool:
        return self._comparison.is_greater_than_equal_to(other)

    def __gt__(self, other: interface.Date) -> bool:
        return self._comparison.is_greater_than(other)
