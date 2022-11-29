import calendar
import re
from src.main.time.dates.formats.interface.format import DateFormat


class DDMMYY(DateFormat):
    def __init__(self, date: str):
        self._date = date

    @property
    def day(self) -> int:
        return int(self._date[0:2])

    @property
    def month(self) -> int:
        return int(self._date[2:4])

    @property
    def year(self) -> int:
        return int(self._date[4:6])


class DDMMYYYY(DDMMYY):
    def __init__(self, date: str):
        super(DDMMYYYY, self).__init__(date)

    @property
    def year(self) -> int:
        return int(self._date[4:8])


class NumericDelimited(DateFormat):
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
        return self._parts[2]


class AlphanumericFormat(DateFormat):
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
        return self._parts[2]
