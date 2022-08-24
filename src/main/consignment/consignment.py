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

    def _set_reference(self, new_reference: str):
        self._reference = (
            new_reference if new_reference.upper().startswith("GR")
            else "GR" + new_reference
        )

    def _strip_reference_prefix(self, ref: str):
        starting_index = 2 if ref.upper().startswith("GR") else 0

        return ref[starting_index:]

    def _is_reference_valid(self, ref: str):
        reference_to_process = self._strip_reference_prefix(ref)
        nine_digit_pattern = re.compile(r"\d{9}")

        return bool(nine_digit_pattern.match(reference_to_process))

    @staticmethod
    def from_fcl_csv(csv_path: str):
        consignment = Consignment()

        return consignment
