from src.main.upn.api.structures.network_pallet.structure import NetworkPallet

from src.main.upn.api.structures.network_pallet.mapping \
    import NetworkPalletStructure


class NetworkPalletParser:
    def __init__(self):
        self._structure = NetworkPalletStructure()

    def parse(self, parse_values: dict[str, str]):
        result = NetworkPallet()

        return result
