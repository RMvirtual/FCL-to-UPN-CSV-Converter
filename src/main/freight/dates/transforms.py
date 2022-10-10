import re
import calendar


def parse(date: str) -> tuple[int, int, int]:
    return DateParser(date).parse()


class DateParser:
    def __init__(self, date: str):
        self._date = date.strip()
        self._validation = DateValidation(self._date)
        self._transformation = DateTransformation(self._date)

    def parse(self) -> tuple[int, int, int]:
        if self._validation.is_ddmmyyyy():
            return self._transformation.dd_mm_yyyy()

        elif self._validation.is_ddmmyy():
            return self._transformation.dd_mm_yy()

        elif self._validation.is_ddmmyy_with_separators():
            return self._transformation.dd_mm_yy_with_separators()

        elif self._validation.is_ddmmyyyy_with_separators():
            return self._transformation.dd_mm_yyyy_with_separators()

        elif self._validation.is_ddmmmyyyy():
            return self._transformation.dd_mmm_yyyy()

        elif self._validation.is_ddmmmyy():
            return self._transformation.dd_mmm_yy()

        elif self._validation.is_full_month():
            return self._transformation.full_month()

        else:
            raise ValueError("Cannot parse date from value of " + self._date)


class DateValidation:
    def __init__(self, date: str):
        self._date = date

    def is_ddmmyy(self) -> bool:
        return re.fullmatch(r"\d{6}", self._date)

    def is_ddmmyy_with_separators(self) -> bool:
        return re.fullmatch(r"\d{2}[./\\-]\d{2}[./\\-]\d{2}", self._date)

    def is_ddmmyyyy(self) -> bool:
        return re.fullmatch(r"\d{8}", self._date)

    def is_ddmmyyyy_with_separators(self) -> bool:
        return re.fullmatch(r"\d{2}[./\\-]\d{2}[./\\-]\d{4}", self._date)

    def is_ddmmmyyyy(self) -> bool:
        return re.fullmatch(
            r"\d{1,2}[./\\-][a-zA-z]{3,9}[./\\-]\d{4}", self._date)

    def is_ddmmmyy(self) -> bool:
        return re.fullmatch(
            r"\d{1,2}[./\\-][a-zA-z]{3,9}[./\\-]\d{2}", self._date)

    def is_full_month(self) -> bool:
        return re.fullmatch(
            r"\d{1,2}\s+[a-zA-z]{3,9}\s+\d{4}", self._date)


class DateTransformation:
    def __init__(self, date: str):
        self._date = date
        self._month_abbreviations = list(calendar.month_abbr)
        self._month_names = list(calendar.month_name)

    def dd_mm_yyyy(self):
        return (
            int(self._date[0:2]),
            int(self._date[2:4]),
            int(self._date[4:8])
        )

    def dd_mm_yy(self):
        return (
            int(self._date[0:2]),
            int(self._date[2:4]),
            int("20" + self._date[4:6])
        )

    def dd_mm_yy_with_separators(self):
        day, month, year = self._split_by_separator_characters()

        return int(day), int(month), int("20" + str(year))

    def dd_mm_yyyy_with_separators(self):
        return tuple(map(int, self._split_by_separator_characters()))

    def dd_mmm_yyyy(self):
        return self._values_by_split_separator()

    def dd_mmm_yy(self):
        day, month, year = self._values_by_split_separator()

        return int(day), month, int("20" + str(year))

    def full_month(self):
        return self._values_by_split_separator()

    def _values_by_split_separator(self) -> tuple[int, int, int]:
        day, month_name, year = self._split_by_separator_characters()

        month = self.month_to_index(month_name)

        return int(day), month, int(year)

    def month_to_index(self, month_name: str) -> int:
        if month_name in self._month_abbreviations:
            month_name = self._month_abbreviations.index(month_name)

        else:
            month_name = self._month_names.index(month_name)

        return int(month_name)

    def _split_by_separator_characters(self) -> tuple[str, str, str]:
        return re.split(r"\s|[./\\-]", self._date)
