import re


def parse(date: str) -> tuple[int, int, int]:
    if re.fullmatch(r"\d{1,2}\d{1,2}(\d{2}|\d{4})", date):
        return int(date[0:2]), int(date[2:4]), int(date[4:8])

    else:
        return None
