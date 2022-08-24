import re


class Reference:
    def __init__(self, reference: str):
        self._prefix = "GR"
        self._number = reference

    def as_string(self):
        return self._prefix + self._number

    @staticmethod
    def _strip_reference_prefix(reference: str):
        starting_index = 2 if reference.upper().startswith("GR") else 0

        return reference[starting_index:]

    @staticmethod
    def is_valid(reference: str):
        reference_to_process = Reference._strip_reference_prefix(reference)
        nine_digit_pattern = re.compile(r"\d{9}")

        return bool(nine_digit_pattern.fullmatch(reference_to_process))

    def _set_reference(self, reference: str):
        self._reference = (
            reference if reference.upper().startswith(self._prefix)
            else self._prefix + reference
        )