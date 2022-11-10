from src.main.upn.api.data_structures.network_pallet import interface
from src.main.upn.api.data_structures.network_pallet.structure \
    import NetworkPallet


class UpnNetworkPalletMarshaller:
    def __init__(self):
        self._interface = interface.network_pallet()

    def unmarshall(self, candidate: dict):
        return None

