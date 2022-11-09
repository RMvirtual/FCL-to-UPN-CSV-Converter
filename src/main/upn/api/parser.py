from src.main.upn.api.structures.network_consignment.structure \
    import NetworkConsignment

from src.main.upn.api.structures.network_consignment.mapping \
    import NetworkConsignmentStructure

class UpnApiParser:
    def __init__(self):
        pass

    def network_consignment(self, parse_values: dict) -> NetworkConsignment:
        result = NetworkConsignment()

        return result

    def barcode(self, parse_values: dict):
        structure = NetworkConsignmentStructure()
        barcode = parse_values[structure.consignment_barcode_no.mapping]

        return barcode
