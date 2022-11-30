from src.main.time.years import validation


def pad_string(year: str) -> str:
    validation.assert_year_is_valid(year)

    return "20" + year if validation.is_valid_short_string(year) else year


def pad_integer(year: int) -> int:
    validation.assert_year_is_valid(year)

    return 2000 + year if validation.is_valid_short_integer(year) else year
