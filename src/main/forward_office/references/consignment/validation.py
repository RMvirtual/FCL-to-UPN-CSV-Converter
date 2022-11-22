import re


class FCLReferenceValidationStrategy:
    def __init__(self):
        self._initialise_matching_patterns()

    def _initialise_matching_patterns(self) -> None:
        self._full_reference_pattern = re.compile(r"[gG][rR]\d{9}")
        self._numbers_only_pattern = re.compile(r"\d{9}")

    def is_valid_reference(self, reference: str) -> bool:
        return self.matches_full(reference) or self.matches_numeric(reference)

    def matches_full(self, reference: str) -> bool:
        return bool(self._full_reference_pattern.fullmatch(reference))

    def matches_numeric(self, reference: str) -> bool:
        return bool(self._numbers_only_pattern.fullmatch(reference))
