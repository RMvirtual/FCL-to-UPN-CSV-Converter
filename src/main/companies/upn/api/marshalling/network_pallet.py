from src.main.companies.upn.api.mapping import network_pallet
from src.main.companies.upn.api.implementation.pallets.download import factory
from src.main.companies.upn.api.interface.pallets.base import NetworkPallet

UPNDict = dict[str, any]


class UpnNetworkPalletMarshaller:
    def __init__(self):
        self._mappings = network_pallet.network_pallet_constraints()

    def unmarshall(self, candidate: dict) -> NetworkPallet:
        result = factory.network_pallet(
            type_name=candidate[self._mappings.type.mapping],
            size_name=candidate[self._mappings.size.mapping]
        )

        result.barcode = candidate[self._mappings.barcode.mapping]
        result.consignment_barcode = candidate[
            self._mappings.consignment_barcode.mapping]

        return result
