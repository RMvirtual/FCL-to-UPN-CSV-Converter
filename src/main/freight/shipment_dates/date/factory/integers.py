import calendar
from src.main.freight.shipment_dates.date.implementation.types \
    import DatesAsIntegers

from src.main.freight.shipment_dates.date.factory.strings \
    import DateAsStringsFactory


class DateAsIntegersFactory:
    def __init__(self, date: str):
        self._date = date
        self._month_abbreviations = list(calendar.month_abbr)
        self._month_names = list(calendar.month_name)
        self._date_as_strings = DateAsStringsFactory(date)

    def from_dd_mm_yy(self) -> DatesAsIntegers:
        result = self._extract_as_numeric_yy()
        result.pad_year()

        return result

    def from_dd_mm_yyyy(self) -> DatesAsIntegers:
        return self._extract_as_numeric_yyyy()

    def from_dd_mm_yy_with_separators(self) -> DatesAsIntegers:
        result = self._extract_as_numeric_with_separators()
        result.pad_year()

        return result

    def from_dd_mm_yyyy_with_separators(self) -> DatesAsIntegers:
        return self._extract_as_numeric_with_separators()

    def from_dd_mmm_yyyy(self) -> DatesAsIntegers:
        return self._extract_as_alphabetical()

    def from_dd_mmm_yy(self) -> DatesAsIntegers:
        result = self._extract_as_alphabetical()
        result.pad_year()

        return result

    def from_full_month(self) -> DatesAsIntegers:
        return self._extract_as_alphabetical()

    def _extract_as_numeric_yyyy(self) -> DatesAsIntegers:
        return self._date_as_strings.dd_mm_yyyy().to_integers()

    def _extract_as_numeric_yy(self) -> DatesAsIntegers:
        return self._date_as_strings.dd_mm_yy().to_integers()

    def _extract_as_numeric_with_separators(self) -> DatesAsIntegers:
        return self._date_as_strings.by_separator_characters().to_integers()

    def _extract_as_alphabetical(self) -> DatesAsIntegers:
        dates = self._date_as_strings.by_separator_characters()
        dates.month = self._alphabetic_month_index(dates.month)

        return dates.to_integers()

    def _alphabetic_month_index(self, month_name: str) -> int:
        is_abbreviated = month_name in self._month_abbreviations

        months = (
            self._month_abbreviations if is_abbreviated else self._month_names)

        return months.index(month_name)

