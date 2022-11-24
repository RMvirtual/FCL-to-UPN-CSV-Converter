from src.main.upn.consignment.structures.cargo.package.network_pallet\
    .implementation \
    import UPNPallet, NetworkPalletFields

from src.main.upn.api.data_structures.network_pallet import mapping


class NetworkPallet1(UPNPallet):
    def __init__(self):
        super().__init__(self._network_pallet_fields())

    @staticmethod
    def _network_pallet_fields() -> NetworkPalletFields:
        result = NetworkPalletFields()
        result.barcode = ""
        result.consignment_barcode = ""

        network_pallet_interface = mapping.network_pallet()
        result.types = network_pallet_interface.type.values
        result.sizes = network_pallet_interface.size.values
        result.type = result.types[0]
        result.size = result.sizes[0]

        return result
