from __future__ import annotations
import datetime


class Date:
    def __init__(self, date: str):
        day, month, year = self._parse_date(date)
        self._date = datetime.date(day=day, month=month, year=year)

    @staticmethod
    def _parse_date(stripped_date: str) -> tuple[int, int, int]:
        stripped_date = stripped_date.replace("/", "")
        day = int(stripped_date[0:2])
        month = int(stripped_date[2:4])
        year = int(stripped_date[4:8])

        return day, month, year

    @property
    def day(self) -> int:
        return self._date.day

    @property
    def month(self) -> int:
        return self._date.month

    @property
    def year(self) -> int:
        return self._date.year

    def __sub__(self, other: Date) -> int:
        other_date = datetime.date(
            day=other.day, month=other.month, year=other.year)

        return abs((self._date - other_date).days)

    def __eq__(self, other: Date) -> bool:
        return (
            self.day == other.day and self.month == other.month
            and self.year == other.year
        )

    def __lt__(self, other: Date) -> bool:
        return (
            True if self.year < other.year else
            True if self.month < other.month
            else self.day < other.day
        )

    def __le__(self, other: Date) -> bool:
        return self < other or self == other

    def __ge__(self, other: Date) -> bool:
        return self > other or self == other

    def __gt__(self, other: Date) -> bool:
        return not self <= other


class ShipmentDates:
    def __init__(self):
        self._collection_date: Date or None = None
        self._delivery_date: Date or None = None
        self._delivery_time: datetime.time or None = None

    @property
    def delivery_date(self) -> Date:
        return self._delivery_date

    @delivery_date.setter
    def delivery_date(self, new_date: Date) -> None:
        self._delivery_date = new_date

    @property
    def collection_date(self) -> Date:
        return self._collection_date

    @collection_date.setter
    def collection_date(self, new_date: Date) -> None:
        self._collection_date = new_date

    @property
    def delivery_time(self) -> datetime.time:
        return self._delivery_time

    @delivery_time.setter
    def delivery_time(self, new_time: datetime.time) -> None:
        self._delivery_time = new_time
