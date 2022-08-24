import re


class Reference:
    def __init__(self, reference: str):
        if Reference._is_valid(reference):
            self._set_reference(reference)

        else:
            raise ValueError(
                "Incorrect reference format. Should be either GRddddddddd "
                + "or ddddddddd"
            )

    def as_string(self):
        return self._prefix + self._number

    @staticmethod
    def _strip_reference_prefix(reference: str):
        starting_index = 2 if reference.upper().startswith("GR") else 0

        return reference[starting_index:]

    @staticmethod
    def _is_valid(reference: str):
        gr_pattern = re.compile(r"\d{9}|[gG][rR]\d{9}")

        return bool(gr_pattern.fullmatch(reference))

    def _set_reference(self, reference: str):
        self._prefix = "GR"

        self._number = (
            reference[2:] if reference.upper().startswith(self._prefix)
            else reference
        )