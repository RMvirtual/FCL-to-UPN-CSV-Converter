from __future__ import annotations
import datetime


class Date:
    def __init__(self, date: str):
        date = date.replace("/", "")
        day = int(date[0:2])
        month = int(date[2:4])
        year = int(date[4:8])

        self._date = datetime.date(day=day, month=month, year=year)

    @property
    def day(self) -> int:
        return self._date.day

    @property
    def month(self) -> int:
        return self._date.month

    @property
    def year(self) -> int:
        return self._date.year

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
        if self.year > other.year:
            return True

        elif self.year == other.year:
            if self.month > other.month:
                return True

            elif self.month == other.month:
                if self.day > other.day:
                    return True

        return False



class ShipmentDates:
    def __init__(self):
        self._collection_date: Date or None = None
        self._delivery_date: Date or None = None
        self._delivery_time: Date or None = None

    @property
    def delivery_date(self) -> datetime.date:
        return self._delivery_date

    @delivery_date.setter
    def delivery_date(self, new_date: datetime.date) -> None:
        self._delivery_date = new_date

    @property
    def collection_date(self) -> datetime.date:
        return self._collection_date

    @collection_date.setter
    def collection_date(self, new_date: datetime.date) -> None:
        self._collection_date = new_date

    @property
    def delivery_time(self) -> datetime.time:
        return self._delivery_time

    @delivery_time.setter
    def delivery_time(self, new_time: datetime.time) -> None:
        self._delivery_time = new_time
