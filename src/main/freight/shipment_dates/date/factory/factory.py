from src.main.freight.shipment_dates.date.factory.integers \
    import DateAsIntegersFactory

from src.main.freight.shipment_dates.date.implementation import types
from src.main.freight.shipment_dates.date.model.format_recognition \
    import DateFormatRecognition


class DateFactory:
    def __init__(self):
        ...


def parse(date: str) -> types.DatesAsIntegers:
    return DateParser(date).parse()


class DateParser:
    def __init__(self, date: str):
        self._date = date.strip()
        self._date_format = DateFormatRecognition(self._date)
        self._transformation = DateAsIntegersFactory(self._date)

    def parse(self) -> types.DatesAsIntegers:
        if self._date_format.is_ddmmyy():
            return self._transformation.from_dd_mm_yy()

        elif self._date_format.is_ddmmyyyy():
            return self._transformation.from_dd_mm_yyyy()

        elif self._date_format.is_ddmmyy_with_separators():
            return self._transformation.from_dd_mm_yy_with_separators()

        elif self._date_format.is_ddmmyyyy_with_separators():
            return self._transformation.from_dd_mm_yyyy_with_separators()

        elif self._date_format.is_ddmmmyyyy():
            return self._transformation.from_dd_mmm_yyyy()

        elif self._date_format.is_ddmmmyy():
            return self._transformation.from_dd_mmm_yy()

        elif self._date_format.is_full_month():
            return self._transformation.from_full_month()

        else:
            raise ValueError("Cannot parse date from value of " + self._date)
