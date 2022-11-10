from src.main.upn.api.structures.network_pallet.structure import NetworkPallet

from src.main.upn.api.structures.network_pallet.mapping \
    import NetworkPalletStructure


class NetworkPalletParser:
    def __init__(self):
        self._structure = NetworkPalletStructure()

    def parse(self, parse_values: dict[str, str]):
        result = NetworkPallet()

        result.consignment_barcode_no = parse_values[
            self._structure.consignment_barcode_no.mapping]

        result.pallet_type = parse_values[self._structure.pallet_type.mapping]
        result.pallet_size = parse_values[self._structure.pallet_size.mapping]

        result.pallet_barcode_no = parse_values[
            self._structure.pallet_barcode_no.mapping]

        # Could also determine whether the parsed values are valid here
        # based off the structure instance values.

        return result
