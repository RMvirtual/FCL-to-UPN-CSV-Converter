import re
import calendar
import dataclasses

from src.main.graylaw.shipment_dates.date.format_recognition \
    import DateFormatRecognition


@dataclasses.dataclass
class DatesAsIntegers:
    day: int = 0
    month: int = 0
    year: int = 0

    def pad_year(self) -> None:
        self.year = int("20" + str(self.year)) \
            if len(str(self.year)) == 2 else self.year


@dataclasses.dataclass
class DatesAsStrings:
    day: str = ""
    month: str = ""
    year: str = ""

    def to_integers(self) -> DatesAsIntegers:
        result = DatesAsIntegers()

        result.day = int(self.day)
        result.month = int(self.month)
        result.year = int(self.year)

        return result


def parse(date: str) -> DatesAsIntegers:
    return DateParser(date).parse()


class DateParser:
    def __init__(self, date: str):
        self._date = date.strip()
        self._date_format = DateFormatRecognition(self._date)
        self._transformation = DateTransformation(self._date)

    def parse(self) -> DatesAsIntegers:
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


class DateTransformation:
    def __init__(self, date: str):
        self._date = date
        self._month_abbreviations = list(calendar.month_abbr)
        self._month_names = list(calendar.month_name)

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
        return self._split_as_dd_mm_yyyy().to_integers()

    def _extract_as_numeric_yy(self) -> DatesAsIntegers:
        return self._split_as_dd_mm_yy().to_integers()

    def _extract_as_numeric_with_separators(self) -> DatesAsIntegers:
        return self._split_by_separator_characters().to_integers()

    def _extract_as_alphabetical(self) -> DatesAsIntegers:
        dates = self._split_by_separator_characters()
        dates.month = self._alphabetic_month_index(dates.month)

        return dates.to_integers()

    def _alphabetic_month_index(self, month_name: str) -> int:
        is_abbreviated = month_name in self._month_abbreviations

        months = (
            self._month_abbreviations if is_abbreviated else self._month_names)

        return months.index(month_name)

    def _split_as_dd_mm_yy(self) -> DatesAsStrings:
        result = DatesAsStrings()
        result.day = self._date[0:2]
        result.month = self._date[2:4]
        result.year = self._date[4:6]

        return result

    def _split_as_dd_mm_yyyy(self) -> DatesAsStrings:
        result = DatesAsStrings()
        result.day = self._date[0:2]
        result.month = self._date[2:4]
        result.year = self._date[4:8]

        return result

    def _split_by_separator_characters(self) -> DatesAsStrings:
        split_values = re.split(r"\s|[./\\-]", self._date)

        result = DatesAsStrings()
        result.day = split_values[0]
        result.month = split_values[1]
        result.year = split_values[2]

        return result
