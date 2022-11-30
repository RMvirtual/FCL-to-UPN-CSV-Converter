from src.main.time.dates.formats.interface import DateFormatter
from src.main.time.dates.formats.recognition import DateFormat
from src.main.time.dates.formats.implementation import (
    NumericFormatter, NumericDelimitedFormatter, AlphanumericFormatter)


def formatter(date: str) -> DateFormatter:
    date_format = DateFormat(date)

    if date_format.is_unrecognised():
        raise ValueError("Cannot format date of " + date)

    if date_format.is_numeric():
        return NumericFormatter(date)

    if date_format.is_numeric_delimited():
        return NumericDelimitedFormatter(date)

    if date_format.is_alphanumeric():
        return AlphanumericFormatter(date)
