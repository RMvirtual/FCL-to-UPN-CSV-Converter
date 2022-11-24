import copy
from src.main.upn.consignment.structures.cargo.package.network_pallet\
    .interface import NetworkPallet as NetworkPalletInterface

from src.main.upn.consignment.structures.cargo.package.pallet.interface \
    import UPNPalletFields


class NetworkPalletFields(UPNPalletFields):
    barcode = ""
    consignment_barcode = ""


class NetworkPallet(NetworkPalletInterface):
    def __init__(self, pallet_fields: NetworkPalletFields):
        super(NetworkPallet, self).__init__(pallet_fields)
        self._barcode = pallet_fields.barcode
        self._consignment_barcode = pallet_fields.consignment_barcode

    @NetworkPalletInterface.barcode.getter
    def barcode(self) -> str:
        return self._barcode

    @NetworkPalletInterface.barcode.setter
    def barcode(self, new_barcode) -> None:
        self._barcode = new_barcode

    @NetworkPalletInterface.consignment_barcode.getter
    def consignment_barcode(self) -> str:
        return self._consignment_barcode

    @NetworkPalletInterface.consignment_barcode.setter
    def consignment_barcode(self, new_barcode):
        self._consignment_barcode = new_barcode

    @NetworkPalletInterface.size.getter
    def size(self) -> str:
        return self._size

    @NetworkPalletInterface.size.setter
    def size(self, new_size: str) -> None:
        self._raise_exception_if_invalid_size(new_size)
        self._size = new_size

    @NetworkPalletInterface.type.getter
    def type(self) -> str:
        return self._type

    @NetworkPalletInterface.type.setter
    def type(self, new_type: str) -> None:
        self._raise_exception_if_invalid_type(new_type)
        self._type = new_type

    @NetworkPalletInterface.types.getter
    def types(self) -> list[str]:
        return copy.deepcopy(self._type_constraints)

    @NetworkPalletInterface.sizes.setter
    def sizes(self) -> list[str]:
        return copy.deepcopy(self._size_constraints)

    def __eq__(self, other: NetworkPalletInterface):
        return (
            super.__eq__(self, other)
            and self.barcode == other.barcode
            and self.consignment_barcode == other.consignment_barcode
        )

    def _raise_exception_if_invalid_type(self, type_name: str) -> None:
        if type_name not in self._type_constraints:
            raise ValueError(
                f"Type {type_name} is invalid. "
                f"Valid types are [{self._type_constraints}]."
            )

    def _raise_exception_if_invalid_size(self, size_name: str) -> None:
        if size_name not in self._size_constraints:
            raise ValueError(
                f"Size {size_name} is invalid. "
                f"Valid sizes are [{self._size_constraints}]"
            )
