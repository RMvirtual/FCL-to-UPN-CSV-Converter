import calendar
import re
from src.main.time.dates.formats.interface import DateFormatter


def _pad_year(year: str or int) -> int:
    is_integer = isinstance(year, int)
    is_string = isinstance(year, str)
    is_invalid_type = not (is_integer or is_string)

    if is_invalid_type:
        raise TypeError("Invalid type for year", year)

    if is_string:
        return int(_pad_string(year))

    return _pad_integer(year)


def _pad_string(year: str) -> str:
    if not bool(re.fullmatch(r"\d{2}|\d{4}", year)):
        raise ValueError(
            f"Invalid date format {year} (should be 2 or 4 digits).")

    return "20" + year if bool(re.fullmatch(r"\d{2}", year)) else year


def _pad_integer(year: int) -> int:
    is_valid_short_year = 0 <= year <= 99
    is_valid_full_year = year >= 1822
    is_invalid_year = not (is_valid_short_year or is_valid_full_year)

    if is_invalid_year:
        raise ValueError("Invalid year", year)

    return 2000 + year if is_valid_short_year else year


class NumericFormatter(DateFormatter):
    def __init__(self, date: str):
        self._assert_format_is_valid(date)
        self._date = date
        self._parts = []
        self._parts.append(self._date[0:2])
        self._parts.append(self._date[2:4])
        self._parts.append(self._date[4:])

    @property
    def day(self) -> int:
        return int(self._parts[0])

    @property
    def month(self) -> int:
        return int(self._parts[1])

    @property
    def year(self) -> int:
        return _pad_year(self._parts[2])

    @staticmethod
    def _assert_format_is_valid(date: str) -> None:
        if not bool(re.fullmatch(r"\d{6,8}", date)):
            raise ValueError("Incorrect number of digits (must be 6 or 8).")


class NumericDelimitedFormatter(DateFormatter):
    def __init__(self, date: str):
        self._date = date
        split_parts = re.split(r"\W+", self._date)
        self._parts = list(map(int, filter(lambda d: bool(d), split_parts)))

    @property
    def day(self) -> int:
        return self._parts[0]

    @property
    def month(self) -> int:
        return self._parts[1]

    @property
    def year(self) -> int:
        return _pad_year(self._parts[2])


class AlphanumericFormatter(DateFormatter):
    def __init__(self, date: str):
        self._date = date
        split_parts = re.split(r"\W+", self._date)
        cleaned_parts = list(filter(lambda d: bool(d), split_parts))
        self._parts = []
        self._parts.append(int(cleaned_parts[0]))

        full_months = dict(
            (month, index)
            for index, month in enumerate(calendar.month_name) if month
        )

        abbreviated_months = dict(
            (month, index)
            for index, month in enumerate(calendar.month_abbr) if month
        )

        month_part = cleaned_parts[1]

        month_no = (
            full_months[month_part] if month_part in full_months else
            abbreviated_months[month_part]
        )

        self._parts.append(month_no)
        self._parts.append(int(cleaned_parts[2]))

    @property
    def day(self) -> int:
        return self._parts[0]

    @property
    def month(self) -> int:
        return self._parts[1]

    @property
    def year(self) -> int:
        return _pad_year(self._parts[2])
