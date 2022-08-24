from src.main.consignment.reference import Reference


class Consignment:
    def __init__(self):
        self._reference: Reference = None

    @property
    def reference(self) -> str:
        return (
            self._reference.string() if self._reference is not None
            else None
        )

    @reference.setter
    def reference(self, new_reference: str):
        try:
            self._reference = Reference(new_reference)

        except ValueError as error:
            raise error
