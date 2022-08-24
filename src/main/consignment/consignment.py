from src.main.consignment.reference import Reference


class Consignment:
    def __init__(self):
        self._reference: Reference = None

    @property
    def reference(self) -> str:
        return self._reference.as_string() if not None else None

    @reference.setter
    def reference(self, new_reference: str):
        if Reference.is_valid(new_reference):
            self._reference = Reference(new_reference)

        else:
            raise ValueError("Incorrect Reference Format")
