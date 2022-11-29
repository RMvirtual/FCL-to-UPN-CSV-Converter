import re
from src.main.freight.shipment_dates.date.implementation.types \
    import DatesAsStrings


class DateAsStringsFactory:
    def __init__(self, date: str):
        self._date = date

    def dd_mm_yy(self) -> DatesAsStrings:
        result = DatesAsStrings()
        result.day = self._date[0:2]
        result.month = self._date[2:4]
        result.year = self._date[4:6]

        return result

    def dd_mm_yyyy(self) -> DatesAsStrings:
        result = DatesAsStrings()
        result.day = self._date[0:2]
        result.month = self._date[2:4]
        result.year = self._date[4:8]

        return result

    def by_separator_characters(self) -> DatesAsStrings:
        split_values = re.split(r"\s|[./\\-]", self._date)

        result = DatesAsStrings()
        result.day = split_values[0]
        result.month = split_values[1]
        result.year = split_values[2]

        return result
