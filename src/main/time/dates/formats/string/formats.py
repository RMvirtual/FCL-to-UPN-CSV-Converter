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
