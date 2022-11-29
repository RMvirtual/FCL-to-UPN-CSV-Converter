from src.main.time.dates.formats.string.recognition import DateFormat
from src.main.time.dates.formats.string.formats import (
    AlphanumericFormat, NumericDelimited, DDMMYY, DDMMYYYY)

from src.main.time.dates.implementation.date import Date
from src.main.time.dates.interface.date import DateInterface


def from_string(date: str) -> DateInterface:
    date_format = DateFormat(date)

    if date_format.is_unrecognised():
        raise ValueError("Cannot parse date with format of " + date)

    formatter = None

    if date_format.is_numeric():
        formatter = DDMMYY(date)

    elif date_format.is_numeric_with_delimiters():
        formatter = NumericDelimited(date)

    elif date_format.is_alphanumeric():
        formatter = AlphanumericFormat(date)

    return Date(formatter.day, formatter.month, formatter.year)


def from_integers(day: int, month: int, year: int):
    return Date(day, month, year)
