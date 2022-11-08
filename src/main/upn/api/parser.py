import dataclasses
from src.main.upn.api import mapping_structures
from src.main.upn.api.mapping_structures import NetworkConsignmentStructure


class UpnApiParser:
    def __init__(self):
        pass

    def network_consignment(
            self, parse_values: dict) -> NetworkConsignmentStructure:
        structure = NetworkConsignmentStructure()

        return structure
