import copy

from src.main.upn.consignment.structures.cargo.package.interface \
    import UPNPallet as UPNPalletInterface

from src.main.upn.consignment.structures.cargo.package.implementation \
    import UPNPallet, UPNPalletFields


class UPNPalletBuilder:
    def __init__(self):
        self._fields = UPNPalletFields()

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

    def build(self) -> UPNPalletInterface:
        return UPNPallet(self._fields)
