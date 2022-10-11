from __future__ import annotations
import datetime

from src.main.freight.shipment_dates import transforms


class Date:
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
    def delivery_date(self, new_date: str) -> None:
        self._delivery_date = Date(new_date)

    @property
    def collection_date(self) -> Date:
        return self._collection_date

    @collection_date.setter
    def collection_date(self, new_date: str) -> None:
        self._collection_date = Date(new_date)

    @property
    def delivery_time(self) -> datetime.time:
        return self._delivery_time

    @delivery_time.setter
    def delivery_time(self, new_time: str) -> None:
        self._delivery_time = datetime.datetime.strptime(new_time, "%I:%M%p")
