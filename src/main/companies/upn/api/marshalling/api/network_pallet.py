from src.main.companies.upn.model.implementation.constraints.implementation \
    import DataConstraint
from src.main.companies.upn.model.implementation.cargo.pallets.download \
    import factory
from src.main.companies.upn.api.interface.cargo.pallets.download \
    import DownloadPallet

UPNDict = dict[str, any]


class UpnNetworkPalletMarshaller:
    def __init__(self):
        self._mappings = network_pallet.network_pallet_constraints()

    def unmarshall(self, candidate: dict) -> DownloadPallet:
        result = factory.network_pallet(
            type_name=candidate[self._mappings.type.mapping],
            size_name=candidate[self._mappings.size.mapping]
        )

        result.barcode = candidate[self._mappings.barcode.mapping]
        result.consignment_barcode = candidate[
            self._mappings.consignment_barcode.mapping]

        return result
