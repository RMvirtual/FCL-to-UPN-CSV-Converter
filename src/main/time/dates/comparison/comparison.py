import datetime
from src.main.time.dates.interface.date import DateInterface


class ComparisonStrategy:
    def __init__(self, date_to_compare: DateInterface):
        self._date_to_compare = date_to_compare

    def is_less_than(self, other: DateInterface) -> bool:
        return (
            True if self._date_to_compare.year < other.year else
            True if self._date_to_compare.month < other.month
            else self._date_to_compare.day < other.day
        )

    def is_less_than_equal_to(self, other: DateInterface) -> bool:
        return self.is_less_than(other) or self.is_equal_to(other)

    def is_equal_to(self, other: DateInterface) -> bool:
        return (
            self._date_to_compare.day == other.day
            and self._date_to_compare.month == other.month
            and self._date_to_compare.year == other.year
        )

    def is_greater_than_equal_to(self, other: DateInterface) -> bool:
        return self.is_greater_than(other) or self.is_equal_to(other)

    def is_greater_than(self, other: DateInterface) -> bool:
        return not self.is_less_than_equal_to(other)

    def difference_in_days(self, other: DateInterface) -> int:
        """Absolute difference in days between the dates."""
        other_datetime = self._datetime_format(other)
        difference = self._datetime_format() - other_datetime

        return abs(difference.days)

    def _datetime_format(self, date: DateInterface = None) -> datetime.date:
        if not date:
            date = self._date_to_compare

        return datetime.date(day=date.day, month=date.month, year=date.year)
