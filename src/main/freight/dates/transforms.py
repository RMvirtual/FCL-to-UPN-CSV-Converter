import re
import calendar


def parse(date: str) -> tuple[int, int, int]:
    cleaned_date = date.strip()

    if _is_ddmmyyyy(cleaned_date):
        return (
            int(cleaned_date[0:2]), int(cleaned_date[2:4]),
            int(cleaned_date[4:8])
        )

    elif _is_ddmmyy(cleaned_date):
        return (
            int(cleaned_date[0:2]),
            int(cleaned_date[2:4]),
            int("20" + cleaned_date[4:6])
        )

    elif _is_ddmmyy_with_separators(cleaned_date):
        day, month, year = _split_by_separator_characters(cleaned_date)

        return int(day), int(month), int("20" + year)

    elif _is_ddmmyyyy_with_separators(cleaned_date):
        day, month, year = _split_by_separator_characters(cleaned_date)

        return int(day), int(month), int(year)

    elif _is_ddmmmyyyy(cleaned_date):
        day, month, year = _split_by_separator_characters(cleaned_date)

        month_abbreviations = list(calendar.month_abbr)
        full_months = list(calendar.month_name)

        if month in month_abbreviations:
            month = month_abbreviations.index(month)

        else:
            month = full_months.index(month)

        return int(day), month, int(year)

    elif _is_ddmmmyy(cleaned_date):
        # dd\mmmmm\yyyy

        day, month, year = _split_by_separator_characters(cleaned_date)

        month_abbreviations = list(calendar.month_abbr)
        full_months = list(calendar.month_name)

        if month in month_abbreviations:
            month = month_abbreviations.index(month)

        else:
            month = full_months.index(month)

        return int(day), month, int("20" + year)

    elif _is_full_month(cleaned_date):
        # dd\mmmmmmmmm\yyyy

        day, month, year = _split_by_whitespace(cleaned_date)

        month_abbreviations = list(calendar.month_abbr)
        full_months = list(calendar.month_name)

        if month in month_abbreviations:
            month = month_abbreviations.index(month)

        else:
            month = full_months.index(month)

        return int(day), month, int(year)

    else:
        raise ValueError("Cannot parse date from value of " + cleaned_date)


def _is_ddmmyy(date: str) -> bool:
    return re.fullmatch(r"\d{6}", date)


def _is_ddmmyy_with_separators(date: str) -> bool:
    return re.fullmatch(r"\d{2}[./\\-]\d{2}[./\\-]\d{2}", date)


def _is_ddmmyyyy(date: str) -> bool:
    return re.fullmatch(r"\d{8}", date)


def _is_ddmmyyyy_with_separators(date: str) -> bool:
    return re.fullmatch(r"\d{2}[./\\-]\d{2}[./\\-]\d{4}", date)


def _is_ddmmmyyyy(date: str) -> bool:
    return re.fullmatch(r"\d{1,2}[./\\-][a-zA-z]{3,9}[./\\-]\d{4}", date)


def _is_ddmmmyy(date: str) -> bool:
    return re.fullmatch(r"\d{1,2}[./\\-][a-zA-z]{3,9}[./\\-]\d{2}", date)


def _is_full_month(date: str) -> bool:
    return re.fullmatch(r"\d{1,2}\s+[a-zA-z]{3,9}\s+\d{4}", date)


def _split_by_separator_characters(value: str) -> tuple[str]:
    return re.split(r"[./\\-]", value)


def _split_by_whitespace(value: str) -> tuple[str]:
    return re.split(r"\s", value)
