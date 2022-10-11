import re


class DateFormatRecognition:
    def __init__(self, date: str):
        self._date = date

    def is_numeric(self) -> bool:
        return re.fullmatch(r"\d{6,8}", self._date)

    def is_alphabetic(self) -> bool:
        return re.fullmatch(
            r"\d{1,2}([./\\-]|\s+)[a-zA-z]{3,9}([./\\-]|\s+)(\d{2}|\d{4})",
            self._date
        )

    def has_separators(self) -> bool:
        return re.fullmatch(
            r"\d{1,2}[./\\-]\d{1,2}[./\\-](\d{2}|\d{4})", self._date)

    def has_whitespace(self) -> bool:
        return re.fullmatch(
            r"\d{1,2}\s+[a-zA-z]{3,9}\s+(\d{2}|\d{4})", self._date)

    def is_ddmmyy(self) -> bool:
        return re.fullmatch(r"\d{6}", self._date)

    def is_ddmmyy_with_separators(self) -> bool:
        return re.fullmatch(r"\d{1,2}[./\\-]\d{1,2}[./\\-]\d{2}", self._date)

    def is_ddmmyyyy(self) -> bool:
        return re.fullmatch(r"\d{8}", self._date)

    def is_ddmmyyyy_with_separators(self) -> bool:
        return re.fullmatch(r"\d{1,2}[./\\-]\d{2}[./\\-]\d{4}", self._date)

    def is_ddmmmyyyy(self) -> bool:
        return re.fullmatch(
            r"\d{1,2}[./\\-][a-zA-z]{3,9}[./\\-]\d{4}", self._date)

    def is_ddmmmyy(self) -> bool:
        return re.fullmatch(
            r"\d{1,2}[./\\-][a-zA-z]{3,9}[./\\-]\d{2}", self._date)

    def is_full_month(self) -> bool:
        return re.fullmatch(
            r"\d{1,2}\s+[a-zA-z]{3,9}\s+\d{4}", self._date)