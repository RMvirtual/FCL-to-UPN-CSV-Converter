

class Consignment:
    def __init__(self):
        self._reference = ""

    @property
    def reference(self):
        return self._reference

    @staticmethod
    def from_upn_csv(csv_path: str):
        consignment = Consignment()

        return consignment
