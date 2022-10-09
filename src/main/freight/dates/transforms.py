import re
import calendar


def parse(date: str) -> tuple[int, int, int]:
    cleaned_date = date.strip()
    date_validation = DateValidation(cleaned_date)
    date_transformation = DateTransformation(cleaned_date)

    if date_validation.is_ddmmyyyy():
        return (
            int(cleaned_date[0:2]),
            int(cleaned_date[2:4]),
            int(cleaned_date[4:8])
        )

    elif date_validation.is_ddmmyy():
        return (
            int(cleaned_date[0:2]),
            int(cleaned_date[2:4]),
            int("20" + cleaned_date[4:6])
        )

    elif date_validation.is_ddmmyy_with_separators():
        day, month, year = date_transformation.split_by_separator_characters()

        return int(day), int(month), int("20" + year)

    elif date_validation.is_ddmmyyyy_with_separators():
        day, month, year = date_transformation.split_by_separator_characters()

        return int(day), int(month), int(year)

    elif date_validation.is_ddmmmyyyy():
        day, month, year = date_transformation.split_by_separator_characters()

        month_abbreviations = list(calendar.month_abbr)
        full_months = list(calendar.month_name)

        if month in month_abbreviations:
            month = month_abbreviations.index(month)

        else:
            month = full_months.index(month)

        return int(day), month, int(year)

    elif date_validation.is_ddmmmyy():
        day, month, year = date_transformation.split_by_separator_characters()

        month_abbreviations = list(calendar.month_abbr)
        full_months = list(calendar.month_name)

        if month in month_abbreviations:
            month = month_abbreviations.index(month)

        else:
            month = full_months.index(month)

        return int(day), month, int("20" + year)

    elif date_validation.is_full_month():
        day, month, year = date_transformation.split_by_separator_characters()

        month_abbreviations = list(calendar.month_abbr)
        full_months = list(calendar.month_name)

        if month in month_abbreviations:
            month = month_abbreviations.index(month)

        else:
            month = full_months.index(month)

        return int(day), month, int(year)

    else:
        raise ValueError("Cannot parse date from value of " + cleaned_date)


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
            r"\d{1,2}[./\\-][a-zA-z]{3,9}[./\\-]\d{4}",self._date)

    def is_ddmmmyy(self) -> bool:
        return re.fullmatch(
            r"\d{1,2}[./\\-][a-zA-z]{3,9}[./\\-]\d{2}", self._date)

    def is_full_month(self) -> bool:
        return re.fullmatch(
            r"\d{1,2}\s+[a-zA-z]{3,9}\s+\d{4}", self._date)


class DateTransformation:
    def __init__(self, date: str):
        self._date = date

    def split_by_separator_characters(self) -> tuple[str]:
        return re.split(r"\s|[./\\-]", self._date)
