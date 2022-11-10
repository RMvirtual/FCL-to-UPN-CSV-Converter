from src.main.upn.api.data_structures.network_pallet import interface

from src.main.upn.api.data_structures.network_pallet.structure \
    import NetworkPallet


class UpnNetworkPalletMarshaller:
    def __init__(self):
        self._interface = interface.network_pallet()

    def unmarshall(self, candidate: dict) -> NetworkPallet:
        result = NetworkPallet()
        result.barcode = candidate[self._interface.barcode.mapping]

        result.consignment_barcode = candidate[
            self._interface.consignment_barcode.mapping]

        result.type = candidate[self._interface.type.mapping]
        result.size = candidate[self._interface.size.mapping]

        return result
