import re


class Reference:
    def __init__(self, reference: str):
        self._initialise_correct_patterns()
        self._initialise(reference)

    def _initialise_correct_patterns(self) -> None:
        self._full_reference_pattern = re.compile(r"[gG][rR]\d{9}")
        self._numbers_only_pattern = re.compile(r"\d{9}")

    def _initialise(self, reference: str) -> None:
        self._prefix = "GR"

        try:
            self._parse_number(reference)

        except ValueError as error:
            raise error

    def _parse_number(self, number) -> None:
        if self._numbers_only_pattern_matches(number):
            self._number = number

        elif self._full_reference_pattern_matches(number):
            self._number = number[2:]

        else:
            raise ValueError(
                "Incorrect reference format. "
                + "Should be either GRddddddddd or ddddddddd."
            )

    def __str__(self) -> str:
        return self.string()

    def string(self) -> str:
        return self._prefix + self._number

    def _full_reference_pattern_matches(self, reference: str) -> bool:
        return bool(self._full_reference_pattern.fullmatch(reference))

    def _numbers_only_pattern_matches(self, number: str) -> bool:
        return bool(self._numbers_only_pattern.fullmatch(number))
