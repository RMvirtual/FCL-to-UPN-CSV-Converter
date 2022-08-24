from src.main.consignment.reference import Reference


class Consignment:
    def __init__(self):
        self._reference: Reference or None = None

    @property
    def reference(self) -> str:
        return None if self._reference is None else str(self._reference)

    @reference.setter
    def reference(self, new_reference: str):
        try:
            self._reference = Reference(new_reference)

        except ValueError as error:
            raise error
