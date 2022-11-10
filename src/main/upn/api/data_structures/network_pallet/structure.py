import copy
from src.main.upn.api.data_structures.network_consignment import interface


class NetworkConsignment:
    def __init__(self):
        upn_interface = interface.NetworkConsignmentInterface()
        self._types = upn_interface.type.values
        self._sizes = upn_interface.size.values
        self._barcode = ""
        self._consignment_barcode = ""
        self._size = self._sizes[0]
        self._type = self._types[0]

