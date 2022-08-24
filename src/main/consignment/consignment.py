import re


class Consignment:
    def __init__(self):
        self._reference = ""

    @property
    def reference(self):
        return self._reference

    @reference.setter
    def reference(self, new_reference: str):
        if self._is_reference_valid(new_reference):
            self._set_reference(new_reference)

        else:
            raise ValueError("Incorrect Reference Format")

    def _set_reference(self, ref: str):
        self._reference = (
            ref if ref.upper().startswith("GR")
            else "GR" + ref
        )

    @staticmethod
    def _strip_reference_prefix(ref: str):
        starting_index = 2 if ref.upper().startswith("GR") else 0

        return ref[starting_index:]

    @staticmethod
    def _is_reference_valid(ref: str):
        reference_to_process = Consignment._strip_reference_prefix(ref)
        nine_digit_pattern = re.compile(r"\d{9}")

        return bool(nine_digit_pattern.fullmatch(reference_to_process))
