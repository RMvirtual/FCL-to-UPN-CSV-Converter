from __future__ import annotations
import copy
from src.main.upn.api.data_structures.network_pallet import interface
from src.main.upn.api.data_structures.network_pallet import mapping

from src.main.upn.api.data_structures.network_pallet.mapping \
    import NetworkPalletMapping


class NetworkPallet(interface.NetworkPallet):
    def __init__(self):
        self._barcode = ""
        self._consignment_barcode = ""
        self._type = None
        self._types = []
        self._size = None
        self._sizes = []

        upn_interface = mapping.network_pallet()
        self._initialise_types(upn_interface)
        self._initialise_sizes(upn_interface)

    def _initialise_types(self, type_map: NetworkPalletMapping) -> None:
        self._types = type_map.type.values
        self._type = self._types[0]

    def _initialise_sizes(self, size_map: NetworkPalletMapping) -> None:
        self._sizes = size_map.size.values
        self._size = self._sizes[0]

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
        self._raise_exception_if_invalid_size(new_size)
        self._size = new_size

    @property
    def sizes(self) -> list[str]:
        return copy.deepcopy(self._sizes)

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, new_type: str) -> None:
        self._raise_exception_if_invalid_type(new_type)
        self._type = new_type

    @property
    def types(self) -> list[str]:
        return copy.deepcopy(self._types)

    def __eq__(self, other: NetworkPallet):
        return (
            self.barcode == other.barcode
            and self.consignment_barcode == other.consignment_barcode
            and self.size == other.size
            and self.type == other.type
        )

    def _raise_exception_if_invalid_type(self, type_name: str) -> None:
        if type_name not in self._types:
            raise ValueError("Type", type_name, "is invalid.")

    def _raise_exception_if_invalid_size(self, size_name: str) -> None:
        if size_name not in self._sizes:
            raise ValueError("Size", size_name, "is invalid.")
