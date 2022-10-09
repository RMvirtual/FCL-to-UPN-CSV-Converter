import re
import calendar


def parse(date: str) -> tuple[int, int, int]:
    date = date.strip()

    if re.fullmatch(r"\d{8}", date):  # ddmmyyyy
        return int(date[0:2]), int(date[2:4]), int(date[4:8])

    elif re.fullmatch(r"\d{6}", date):  # ddmmyy
        return int(date[0:2]), int(date[2:4]), int("20" + date[4:6])

    elif re.fullmatch(r"\d{2}[./\\-]\d{2}[./\\-]\d{2}", date):  # dd\mm\yy
        day, month, year = _split_by_separator_characters(date)

        return int(day), int(month), int("20" + year)

    elif re.fullmatch(r"\d{2}[./\\-]\d{2}[./\\-]\d{4}", date):  # dd\mm\yyyy
        day, month, year = _split_by_separator_characters(date)

        return int(day), int(month), int(year)

    elif re.fullmatch(r"\d{1,2}[./\\-][a-zA-z]{3,9}[./\\-]\d{4}", date):
        # dd\mmm\yyyy

        day, month, year = _split_by_separator_characters(date)

        month_abbreviations = list(calendar.month_abbr)
        full_months = list(calendar.month_name)

        if month in month_abbreviations:
            month = month_abbreviations.index(month)

        else:
            month = full_months.index(month)

        return int(day), month, int(year)

    elif re.fullmatch(r"\d{1,2}[./\\-][a-zA-z]{3,9}[./\\-]\d{2}", date):
        # dd\mmmmm\yyyy

        day, month, year = _split_by_separator_characters(date)

        month_abbreviations = list(calendar.month_abbr)
        full_months = list(calendar.month_name)

        if month in month_abbreviations:
            month = month_abbreviations.index(month)

        else:
            month = full_months.index(month)

        return int(day), month, int("20" + year)

    elif re.fullmatch(r"\d{1,2}\s+[a-zA-z]{3,9}\s+\d{4}", date):
        # dd\mmmmmmmmm\yyyy

        day, month, year = _split_by_whitespace(date)

        month_abbreviations = list(calendar.month_abbr)
        full_months = list(calendar.month_name)

        if month in month_abbreviations:
            month = month_abbreviations.index(month)

        else:
            month = full_months.index(month)

        return int(day), month, int(year)

    else:
        raise ValueError("Cannot parse date from value of" + date)


def _split_by_separator_characters(value: str) -> tuple[str]:
    return re.split(r"[./\\-]", value)


def _split_by_whitespace(value: str) -> tuple[str]:
    return re.split(r"\s", value)
