import datetime
from src.main.graylaw.shipment_dates.date import interface
from src.main.graylaw.shipment_dates.date import transforms


class Date(interface.Date):
    def __init__(self, date: str):
        parsed_date = transforms.parse(date)

        self._date = datetime.date(
            day=parsed_date.day,
            month=parsed_date.month,
            year=parsed_date.year
        )

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
        return (
            self.day == other.day and self.month == other.month
            and self.year == other.year
        )

    def __lt__(self, other: interface.Date) -> bool:
        return (
            True if self.year < other.year else
            True if self.month < other.month
            else self.day < other.day
        )

    def __le__(self, other: interface.Date) -> bool:
        return self < other or self == other

    def __ge__(self, other: interface.Date) -> bool:
        return self > other or self == other

    def __gt__(self, other: interface.Date) -> bool:
        return not self <= other
