from src.main.upn.api.data_structures.network_pallet import interface
from src.main.upn.api.data_structures.network_consignment.structure \
    import NetworkConsignment

from src.main.upn.api.data_structures.network_pallet.marshalling \
    import UpnNetworkPalletMarshaller


class UpnNetworkConsignmentMarshaller:
    def __init__(self):
        self._interface = interface.network_pallet()
        self._pallet_marshaller = UpnNetworkPalletMarshaller()

    def unmarshall(self, candidate: dict) -> NetworkConsignment:
        result = NetworkConsignment()
        result.barcode = candidate[self._interface.barcode.mapping]

        result.consignment_barcode = candidate[
            self._interface.consignment_barcode.mapping]

        result.type = candidate[self._interface.type.mapping]
        result.size = candidate[self._interface.size.mapping]

        return result
