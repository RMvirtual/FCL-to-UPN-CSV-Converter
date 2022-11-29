from src.main.freight.shipment_dates.date.factory.integers \
    import DatesAsIntegersFactory

from src.main.freight.shipment_dates.date.factory.strings \
    import DatesAsStringsFactory

from src.main.freight.shipment_dates.date.implementation import types
from src.main.freight.shipment_dates.date.model.format_recognition \
    import DateFormatRecognition

from src.main.freight.shipment_dates.date.interfaces.interface import Date


class DateFactory:
    def __init__(self):
        self._dates_as_strings = DatesAsStringsFactory()
        self._transformation = DatesAsIntegersFactory()

    def parse(self, date: str) -> types.DatesAsIntegers:
        date_format = DateFormatRecognition(date)

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
