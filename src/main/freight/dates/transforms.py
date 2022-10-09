import re


def parse(date: str) -> tuple[int, int, int]:
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

    else:
        return None


def _split_by_separator_characters(value: str) -> tuple[str]:
    return re.split(r"[./\\-]", value)
