from src.main.time.dates.factory.integers import DatesAsIntegersFactory
from src.main.time.dates.factory.strings import DatesAsStringsFactory
from src.main.time.dates.interface.date import DateInterface
from src.main.time.dates.formats.string.recognition import DateFormatter


class DateFactory:
    def __init__(self):
        self._dates_as_strings = DatesAsStringsFactory()
        self._transformation = DatesAsIntegersFactory()

    def parse(self, date: str) -> DateInterface:
        date_format = DateFormatter(date)

        if date_format.is_ddmmyy():
            return self._transformation.from_dd_mm_yy(date)

        elif date_format.is_ddmmyyyy():
            return self._transformation.from_dd_mm_yyyy(date)

        elif date_format.is_ddmmyy_with_separators():
            return self._transformation.from_dd_mm_yy_with_separators(date)

        elif date_format.is_ddmmyyyy_with_separators():
            return self._transformation.from_dd_mm_yyyy_with_separators(date)

        elif date_format.is_ddmmmyyyy():
            return self._transformation.from_dd_mmm_yyyy(date)

        elif date_format.is_ddmmmyy():
            return self._transformation.from_dd_mmm_yy(date)

        elif date_format.is_full_month():
            return self._transformation.from_full_month(date)

        else:
            raise ValueError("Cannot parse date from value of " + date)
