import re


def parse(date: str) -> tuple[int, int, int]:
    if re.fullmatch(r"\d{2}\d{2}\d{4}", date):  # ddmmyyyy
        return int(date[0:2]), int(date[2:4]), int(date[4:8])

    elif re.fullmatch(r"\d{2}\d{2}\d{2}", date):  # ddmmyy
        return int(date[0:2]), int(date[2:4]), (2000 + int(date[4:6]))

    elif re.fullmatch(r"\d{2}[./\\-]\d{2}[./\\-]\d{2}", date):  # dd\mm\yy
        return int(date[0:2]), int(date[3:5]), (2000 + int(date[6:8]))

    elif re.fullmatch(r"\d{2}[./\\-]\d{2}[./\\-]\d{4}", date):  # dd\mm\yyyy
        return int(date[0:2]), int(date[3:5]), (int(date[6:10]))

    else:
        return None
