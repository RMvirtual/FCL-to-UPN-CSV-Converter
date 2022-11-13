from src.main.upn.api.data_structures.network_consignment import interface

from src.main.upn.api.data_structures.network_consignment.structure \
    import NetworkConsignment


class UpnNetworkConsignmentMarshaller:
    def __init__(self):
        self._interface = interface.network_consignment()

    def unmarshall(self, candidate: dict) -> NetworkConsignment:
        result = NetworkConsignment()
        result.references.barcode = candidate[self._interface.barcode.mapping]

        result.references.consignment_no = candidate[
            self._interface.consignment_no.mapping]

        result.references.customer_reference = candidate[
            self._interface.customer_reference.mapping]

        return result
