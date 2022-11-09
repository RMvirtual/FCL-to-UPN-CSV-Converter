from src.main.upn.api.structures.network_consignment.structure \
    import NetworkConsignment

from src.main.upn.api.structures.network_consignment.mapping \
    import NetworkConsignmentStructure


class NetworkConsignmentParser:
    def __init__(self):
        self._structure = NetworkConsignmentStructure()
        self._consignment = NetworkConsignment()

    def barcode(self, parse_values: dict):
        return parse_values[self._structure.consignment_barcode_no.mapping]

    def consignment_no(self, parse_values: dict):
        return parse_values[self._structure.consignment_no.mapping]

    def customer_name(self, parse_values: dict):
        return parse_values[self._structure.customer_name.mapping]

