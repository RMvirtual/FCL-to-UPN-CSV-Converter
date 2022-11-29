import re
from src.main.time.dates.implementation.types \
    import DatesAsStrings


class DatesAsStringsFactory:
    def __init__(self):
        ...

    def dd_mm_yy(self, date: str) -> DatesAsStrings:
        result = DatesAsStrings()
        result.day = date[0:2]
        result.month = date[2:4]
        result.year = date[4:6]

        return result

    def dd_mm_yyyy(self, date: str) -> DatesAsStrings:
        result = DatesAsStrings()
        result.day = date[0:2]
        result.month = date[2:4]
        result.year = date[4:8]

        return result

    def by_separator_characters(self, date: str) -> DatesAsStrings:
        split_values = re.split(r"\s|[./\\-]", date)

        result = DatesAsStrings()
        result.day = split_values[0]
        result.month = split_values[1]
        result.year = split_values[2]

        return result
