import calendar
from src.main.freight.shipment_dates.date.implementation.types \
    import DatesAsIntegers

from src.main.freight.shipment_dates.date.factory.strings \
    import DatesAsStringsFactory


class DateAsIntegersFactory:
    def __init__(self):
        self._month_abbreviations = list(calendar.month_abbr)
        self._month_names = list(calendar.month_name)
        self._date_as_strings = DatesAsStringsFactory()

    def from_dd_mm_yy(self, date: str) -> DatesAsIntegers:
        result = self._extract_as_numeric_yy(date)
        result.pad_year()

        return result

    def from_dd_mm_yyyy(self, date: str) -> DatesAsIntegers:
        return self._extract_as_numeric_yyyy(date)

    def from_dd_mm_yy_with_separators(self, date: str) -> DatesAsIntegers:
        result = self._extract_as_numeric_with_separators(date)
        result.pad_year()

        return result

    def from_dd_mm_yyyy_with_separators(self, date: str) -> DatesAsIntegers:
        return self._extract_as_numeric_with_separators(date)

    def from_dd_mmm_yyyy(self, date: str) -> DatesAsIntegers:
        return self._extract_as_alphabetical(date)

    def from_dd_mmm_yy(self, date: str) -> DatesAsIntegers:
        result = self._extract_as_alphabetical(date)
        result.pad_year()

        return result

    def from_full_month(self, date: str) -> DatesAsIntegers:
        return self._extract_as_alphabetical(date)

    def _extract_as_numeric_yyyy(self, date: str) -> DatesAsIntegers:
        return self._date_as_strings.dd_mm_yyyy(date).to_integers()

    def _extract_as_numeric_yy(self, date: str) -> DatesAsIntegers:
        return self._date_as_strings.dd_mm_yy(date).to_integers()

    def _extract_as_numeric_with_separators(
            self, date: str) -> DatesAsIntegers:
        return self._date_as_strings.by_separator_characters(date)\
            .to_integers()

    def _extract_as_alphabetical(self, date: str) -> DatesAsIntegers:
        dates = self._date_as_strings.by_separator_characters(date)
        dates.month = self._alphabetic_month_index(dates.month)

        return dates.to_integers()

    def _alphabetic_month_index(self, month_name: str) -> int:
        is_abbreviated = month_name in self._month_abbreviations

        months = (
            self._month_abbreviations if is_abbreviated else self._month_names)

        return months.index(month_name)

