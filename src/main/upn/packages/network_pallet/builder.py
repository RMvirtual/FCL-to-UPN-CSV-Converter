import copy
from src.main.upn.api.interfaces.pallets.network_pallet import NetworkPalletInterface

from src.main.upn.packages.network_pallet.implementation import (
    NetworkPallet, NetworkPalletFields)


class NetworkPalletBuilder:
    def __init__(self):
        self._fields = NetworkPalletFields()

    def set_barcode(self, barcode: str) -> None:
        self._fields.barcode = barcode

    def set_consignment_barcode(self, barcode: str) -> None:
        self._fields.consignment_barcode = barcode

    def set_type(self, type_code: str) -> None:
        self._fields.type = type_code

    def set_size(self, size_code: str) -> None:
        self._fields.size = size_code

    def set_type_constraints(self, types: list) -> None:
        self._fields.types = copy.deepcopy(types)

    def set_size_constraints(self, sizes: list) -> None:
        self._fields.sizes = copy.deepcopy(sizes)

    def build(self) -> NetworkPalletInterface:
        return NetworkPallet(self._fields)
