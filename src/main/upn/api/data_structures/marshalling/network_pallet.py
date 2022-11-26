from src.main.upn.api.data_structures.mapping import network_pallet
from src.main.upn.packages.network_pallet import factory
from src.main.upn.api.data_structures.interfaces.network_pallet \
    import NetworkPalletInterface

UPNDict = dict[str, any]


class UpnNetworkPalletMarshaller:
    def __init__(self):
        self._mappings = network_pallet.network_pallet()

    def unmarshall(self, candidate: dict) -> NetworkPalletInterface:
        result = factory.network_pallet(
            type_name=candidate[self._mappings.type.mapping],
            size_name=candidate[self._mappings.size.mapping]
        )

        result.barcode = candidate[self._mappings.barcode.mapping]
        result.consignment_barcode = candidate[
            self._mappings.consignment_barcode.mapping]

        return result
