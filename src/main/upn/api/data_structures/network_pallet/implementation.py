from src.main.upn.consignment.structures.cargo.package.implementation \
    import UPNPallet, UPNPalletFields

from src.main.upn.api.data_structures.network_pallet import mapping


class NetworkPallet(UPNPallet):
    def __init__(self):
        super().__init__(self._network_pallet_fields())

    @staticmethod
    def _network_pallet_fields() -> UPNPalletFields:
        result = UPNPalletFields()
        result.barcode = ""
        result.consignment_barcode = ""

        network_pallet_interface = mapping.network_pallet()
        result.types = network_pallet_interface.type.values
        result.sizes = network_pallet_interface.size.values
        result.type = result.types[0]
        result.size = result.sizes[0]

        return result
