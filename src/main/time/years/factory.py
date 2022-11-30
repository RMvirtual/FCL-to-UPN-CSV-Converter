from src.main.time.years import padding


def full_year(year: str or int) -> int:
    return (
        int(padding.pad_string(year)) if isinstance(year, str)
        else padding.pad_integer(year)
    )
