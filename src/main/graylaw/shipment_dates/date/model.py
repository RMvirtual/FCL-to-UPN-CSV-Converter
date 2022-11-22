import datetime
from src.main.graylaw.shipment_dates.date import interface
from src.main.graylaw.shipment_dates.date import transforms
from src.main.graylaw.shipment_dates.date.comparison \
    import DateComparisonStrategy


class Date(interface.Date):
    def __init__(self, date: str):
        parsed_date = transforms.parse(date)

        self._date = datetime.date(
            day=parsed_date.day,
            month=parsed_date.month,
            year=parsed_date.year
        )

        self._comparison = DateComparisonStrategy(self)

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
        other_date = datetime.date(
            day=other.day, month=other.month, year=other.year)

        return abs((self._date - other_date).days)

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
