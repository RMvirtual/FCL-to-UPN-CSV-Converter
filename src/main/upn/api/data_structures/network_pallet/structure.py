import copy
from src.main.upn.api.data_structures.network_pallet import interface


class NetworkPallet:
    def __init__(self):
        upn_interface = interface.network_pallet()
        self._types = upn_interface.type.values
        self._sizes = upn_interface.size.values
        self._barcode = ""
        self._consignment_barcode = ""
        self._size = self._sizes[0]
        self._type = self._types[0]

    @property
    def types(self) -> list[str]:
        return copy.copy(self._types)

    @property
    def sizes(self) -> list[str]:
        return copy.copy(self._sizes)

    @property
    def barcode(self) -> str:
        return self._barcode

    @barcode.setter
    def barcode(self, new_barcode) -> None:
        self._barcode = new_barcode

    @property
    def consignment_barcode(self) -> str:
        return self._consignment_barcode

    @consignment_barcode.setter
    def consignment_barcode(self, new_barcode):
        self._consignment_barcode = new_barcode

    @property
    def size(self) -> str:
        return self._size

    @size.setter
    def size(self, new_size: str) -> None:
        if new_size in self._sizes:
            self._size = new_size

        else:
            raise ValueError("Size", new_size, "is invalid.")

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, new_type: str) -> None:
        if new_type in self._types:
            self._type = new_type

        else:
            raise ValueError("Type", new_type, "is invalid.")
