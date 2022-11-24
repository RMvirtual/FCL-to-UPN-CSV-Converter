from src.main.upn.consignment.cargo.package.cust_pallet.interface \
    import CustPallet as CustPalletInterface

from src.main.upn.consignment.cargo.package.pallet.abstract \
    import AbstractUPNPallet, UPNPalletFields


class CustPalletFields(UPNPalletFields):
    weight: int = 0


class CustPallet(AbstractUPNPallet, CustPalletInterface):
    def __init__(self, pallet_fields: CustPalletFields) -> None:
        super().__init__(pallet_fields)
        self._weight = pallet_fields.weight

    @property
    def weight(self) -> int:
        return self._weight

    @weight.setter
    def weight(self, new_weight: int) -> None:
        self._weight = new_weight
