

class Consignment:
    def __init__(self):
        self._reference = ""

    @property
    def reference(self):
        return self._reference

    @reference.setter
    def reference(self, new_reference):
        self._reference = new_reference

    @staticmethod
    def from_fcl_csv(csv_path: str):
        consignment = Consignment()

        return consignment
