import calendar
import re
from src.main.time.dates.formats.interface import DateFormatter


def _pad_year(year: str or int) -> int:
    if isinstance(year, str):
        if not bool(re.fullmatch(r"\d{2, 4}", year)):
            raise ValueError(
                "Invalid date format (should be 2 or 4 numeric digits.")

        if re.fullmatch(r"\d{2}", year):
            return int("20" + year)

        elif re.fullmatch(r"\d{4}", year):
            return int(year)

    elif isinstance(year, int):
        if 0 <= year <= 99:
            return 2000 + year

        elif year > 1822:
            return year

        else:
            raise ValueError("Invalid year", year)


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
