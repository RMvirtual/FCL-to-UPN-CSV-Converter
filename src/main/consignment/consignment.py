import re


class Consignment:
    def __init__(self):
        self._reference = ""

    @property
    def reference(self):
        return self._reference

    @reference.setter
    def reference(self, new_reference: str):
        reference_is_valid = False
        reference_to_process = new_reference

        if new_reference.upper().startswith("GR"):
            reference_to_process = new_reference[2:]

        digit_pattern = re.compile(r"\d{9}")

        if bool(digit_pattern.match(reference_to_process)):
            reference_is_valid = True

        if reference_is_valid:
            self._reference = "GR" + reference_to_process

        else:
            raise ValueError("Incorrect Reference Format")

    @staticmethod
    def from_fcl_csv(csv_path: str):
        consignment = Consignment()

        return consignment
