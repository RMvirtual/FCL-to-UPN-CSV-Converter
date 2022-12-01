import re


class DateFormat:
    def __init__(self, date: str):
        self._date = date.strip()

    def is_numeric(self) -> bool:
        return bool(re.fullmatch(r"\d{6,8}", self._date))

    def is_numeric_delimited(self) -> bool:
        return bool(re.fullmatch(
            r"\d{1,2}([./\\-]|\s+)\d{1,2}([./\\-]|\s+)(\d{2}|\d{4})",
            self._date
        ))

    def is_alphanumeric(self) -> bool:
        return bool(re.fullmatch(
            r"\d{1,2}([./\\-]|\s+)[a-zA-Z]{3,9}([./\\-]|\s+)(\d{2}|\d{4})",
            self._date
        ))

    def is_unrecognised(self) -> bool:
        return not self.is_recognised()

    def is_recognised(self) -> bool:
        return any((
            self.is_numeric(), self.is_numeric_delimited(),
            self.is_alphanumeric()
        ))
