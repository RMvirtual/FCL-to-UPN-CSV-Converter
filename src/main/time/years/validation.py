import re


def is_valid_year(year: int or str) -> bool:
    return is_valid_full_year(year) or is_valid_short_year(year)


def is_valid_full_year(year: int or str) -> bool:
    assert_type_is_valid(year)

    return (
        is_valid_full_integer(year) if _type_is_int(year)
        else is_valid_full_string(year)
    )


def is_valid_short_year(year: int or str) -> bool:
    assert_type_is_valid(year)

    return (
        is_valid_short_integer(year) if _type_is_int(year)
        else is_valid_short_string(year)
    )


def assert_year_is_valid(year: int or str) -> None:
    if not is_valid_year(year):
        raise YearValueInvalid(year)


def is_valid_integer(year: int) -> bool:
    return not (is_valid_short_integer(year) or is_valid_full_integer(year))


def is_valid_full_integer(year: int) -> bool:
    return year >= 1822


def is_valid_short_integer(year: int) -> bool:
    return 0 <= year <= 99


def is_valid_string(year: str) -> bool:
    return bool(re.fullmatch(r"\d{2}|\d{4}", year))


def is_valid_full_string(year: str) -> bool:
    return bool(re.fullmatch(r"\d{4}", year))


def is_valid_short_string(year: str) -> bool:
    return bool(re.fullmatch(r"\d{2}", year))


def assert_type_is_valid(year: str or int) -> None:
    if not is_valid_type(year):
        raise TypeError("Invalid parameter type for year", year)


def is_valid_type(year: str or int) -> bool:
    return _type_is_int(year) or _type_is_string(year)


def _type_is_int(year: int) -> bool:
    return isinstance(year, int)


def _type_is_string(year: str) -> bool:
    return isinstance(year, str)


class YearValueInvalid(ValueError):
    def __init__(self, year: str):
        super().__init__(f"year {year} is invalid")


class YearFormatInvalid(ValueError):
    def __init__(self, year: str):
        super().__init__(
            f"Invalid date format {year} (should be 2 or 4 digits).")
