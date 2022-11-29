import re
from src.main.time.dates.implementation.string import StringDate


class DatesAsStringsFactory:
    def __init__(self):
        ...

    def dd_mm_yy(self, date: str) -> StringDate:
        return StringDate(day=date[0:2], month=date[2:4], year=date[4:6])

    def dd_mm_yyyy(self, date: str) -> StringDate:
        return StringDate(day=date[0:2], month=date[2:4], year=date[4:8])

    def by_separator_characters(self, date: str) -> StringDate:
        split_values = re.split(r"\s|[./\\-]", date)

        return StringDate(
            day=split_values[0], month=split_values[1], year=split_values[2])
