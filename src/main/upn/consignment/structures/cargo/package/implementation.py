import copy
import dataclasses
from src.main.upn.consignment.structures.cargo.package.interface \
    import UPNPallet as UPNPalletInterface


@dataclasses.dataclass
class UPNPalletFields:
    barcode = ""
    consignment_barcode = ""
    type = ""
    size = ""
    types: list = dataclasses.field(default=list)
    sizes: list = dataclasses.field(default=list)


class UPNPallet(UPNPalletInterface):
    def __init__(self, pallet_fields: UPNPalletFields):
        self._barcode = pallet_fields.barcode
        self._consignment_barcode = pallet_fields.consignment_barcode
        self._types = pallet_fields.types
        self._type = pallet_fields.type
        self._sizes = pallet_fields.sizes
        self._size = pallet_fields.size

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

    def __eq__(self, other: UPNPalletInterface):
        return (
            self.barcode == other.barcode
            and self.consignment_barcode == other.consignment_barcode
            and self.size == other.size
            and self.type == other.type
        )

    def _raise_exception_if_invalid_type(self, type_name: str) -> None:
        if type_name not in self._types:
            raise ValueError(
                f"Type {type_name} is invalid. "
                f"Valid types are [{self._types}]."
            )

    def _raise_exception_if_invalid_size(self, size_name: str) -> None:
        if size_name not in self._sizes:
            raise ValueError(
                f"Size {size_name} is invalid. "
                f"Valid sizes are [{self._sizes}]"
            )
