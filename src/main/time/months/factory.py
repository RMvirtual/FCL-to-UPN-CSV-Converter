import calendar


def month_no(month_name: str) -> int:
    return MonthIndexes()[month_name]


class MonthIndexes:
    def __init__(self):
        self._names_to_indexes = {}
        self._initialise_full_names()
        self._initialise_abbreviations()

    def _initialise_full_names(self) -> None:
        self._names_to_indexes.update(dict(
            (month, index)
            for index, month in enumerate(calendar.month_name) if month
        ))

    def _initialise_abbreviations(self) -> None:
        self._names_to_indexes.update(dict(
            (month, index)
            for index, month in enumerate(calendar.month_abbr) if month
        ))

    def __getitem__(self, month_name: str) -> int:
        return self._names_to_indexes[month_name]
