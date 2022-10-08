import re


def parse(date: str) -> tuple[int, int, int]:
    if re.fullmatch(r"\d{8}", date):  # ddmmyyyy
        return int(date[0:2]), int(date[2:4]), int(date[4:8])

    elif re.fullmatch(r"\d{6}", date):  # ddmmyy
        return int(date[0:2]), int(date[2:4]), (2000 + int(date[4:6]))

    elif re.fullmatch(r"\d{2}[./\\-]\d{2}[./\\-]\d{2}", date):  # dd\mm\yy
        day, month, year = re.split(r"[./\\-]", date)

        return int(day), int(month), (2000 + int(year))

    elif re.fullmatch(r"\d{2}[./\\-]\d{2}[./\\-]\d{4}", date):  # dd\mm\yyyy
        day, month, year = re.split(r"[./\\-]", date)

        return int(day), int(month), int(year)

    else:
        return None
