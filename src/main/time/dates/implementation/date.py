import datetime
from src.main.time.dates.interface.date import DateInterface
from src.main.time.dates.comparison.comparison import ComparisonStrategy


class Date(DateInterface):
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

    def __sub__(self, other: DateInterface) -> int:
        return self._comparison.difference_in_days(other)

    def __eq__(self, other: DateInterface) -> bool:
        return self._comparison.is_equal_to(other)

    def __lt__(self, other: DateInterface) -> bool:
        return self._comparison.is_less_than(other)

    def __le__(self, other: DateInterface) -> bool:
        return self._comparison.is_less_than_equal_to(other)

    def __ge__(self, other: DateInterface) -> bool:
        return self._comparison.is_greater_than_equal_to(other)

    def __gt__(self, other: DateInterface) -> bool:
        return self._comparison.is_greater_than(other)
