import re
from src.main.time.dates.formats import validation
from src.main.time.dates.formats.interface import DateFormatter
from src.main.time.months import factory as months_factory
from src.main.time.years import factory as years_factory


class NumericFormatter(DateFormatter):
    def __init__(self, date: str):
        validation.assert_numeric_format_is_valid(date)
        self._day = int(date[0:2])
        self._month = int(date[2:4])
        self._year = years_factory.full_year(date[4:])

    @property
    def day(self) -> int:
        return self._day

    @property
    def month(self) -> int:
        return self._month

    @property
    def year(self) -> int:
        return self._year


class NumericDelimitedFormatter(DateFormatter):
    def __init__(self, date: str):
        date_items = self._itemise_date(date)

        self._day = date_items[0]
        self._month = date_items[1]
        self._year = years_factory.full_year(date_items[2])

    def _itemise_date(self, date: str) -> list[int]:
        return list(map(int, self._split_string_by_non_word_values(date)))

    @staticmethod
    def _split_string_by_non_word_values(string: str) -> filter:
        return filter(lambda part: bool(part), re.split(r"\W+", string))

    @property
    def day(self) -> int:
        return self._day

    @property
    def month(self) -> int:
        return self._month

    @property
    def year(self) -> int:
        return self._year


class AlphanumericFormatter(DateFormatter):
    def __init__(self, date: str):
        date_items = self._itemise_date(date)

        self._day = int(date_items[0])
        self._month = months_factory.month_no(date_items[1])
        self._year = years_factory.full_year(date_items[2])

    def _itemise_date(self, date: str) -> list[str]:
        return list(self._split_string_by_non_words(date))

    @staticmethod
    def _split_string_by_non_words(string: str) -> filter:
        return filter(lambda part: bool(part), re.split(r"\W+", string))

    @property
    def day(self) -> int:
        return self._day

    @property
    def month(self) -> int:
        return self._month

    @property
    def year(self) -> int:
        return self._year
