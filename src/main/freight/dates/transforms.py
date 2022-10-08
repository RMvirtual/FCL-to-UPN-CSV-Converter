import re


def parse(date: str) -> tuple[int, int, int]:
    if re.fullmatch(r"\d{2}\d{2}\d{4}", date):  # ddmmyyyy
        return int(date[0:2]), int(date[2:4]), int(date[4:8])

    elif re.fullmatch(r"\d{2}\d{2}\d{2}", date):  # ddmmyy
        return int(date[0:2]), int(date[2:4]), (2000 + int(date[4:6]))

    else:
        return None
