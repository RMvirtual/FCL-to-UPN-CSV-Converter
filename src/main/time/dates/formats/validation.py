import re


def assert_numeric_format_is_valid(date: str) -> None:
    if not is_valid_numeric_format(date):
        raise NumericFormatInvalid(date)


def is_valid_numeric_format(date: str) -> bool:
    return bool(re.fullmatch(r"\d{6}|\d{8}", date))


class NumericFormatInvalid(ValueError):
    def __init__(self, date: str):
        super().__init__(
            f"Incorrect format for date {date} (must be 6 or 8 digits).")
