from src.main.upn.api.data_structures.interfaces.network_pallet \
    import NetworkPalletInterface

from src.main.upn.freight.cargo.pallet.abstract import (
    UPNPalletFields, AbstractUPNPallet)


class NetworkPalletFields(UPNPalletFields):
    barcode = ""
    consignment_barcode = ""


class NetworkPallet(AbstractUPNPallet, NetworkPalletInterface):
    def __init__(self, pallet_fields: NetworkPalletFields):
        super().__init__(pallet_fields)
        self._barcode = pallet_fields.barcode
        self._consignment_barcode = pallet_fields.consignment_barcode

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

    def __eq__(self, other: NetworkPalletInterface):
        return (
            super.__eq__(self, other)
            and self.barcode == other.barcode
            and self.consignment_barcode == other.consignment_barcode
        )
