from src.main.upn.api.data_structures.network_pallet import mapping

from src.main.upn.api.data_structures.network_pallet.structure \
    import NetworkPallet


class UpnNetworkPalletMarshaller:
    def __init__(self):
        self._mappings = mapping.network_pallet()

    def unmarshall(self, candidate: dict) -> NetworkPallet:
        result = NetworkPallet()
        result.barcode = candidate[self._mappings.barcode.mapping]

        result.consignment_barcode = candidate[
            self._mappings.consignment_barcode.mapping]

        result.type = candidate[self._mappings.type.mapping]
        result.size = candidate[self._mappings.size.mapping]

        return result
