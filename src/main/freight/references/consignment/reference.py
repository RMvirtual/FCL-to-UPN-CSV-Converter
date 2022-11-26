from src.main.freight.references import interface


class ConsignmentReference(interface.ConsignmentReference):
    def __init__(self, reference: str):
        self._reference = reference

    def __str__(self):
        return self._reference

