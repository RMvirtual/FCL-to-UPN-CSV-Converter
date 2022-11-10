import unittest
from src.main.upn.api.parser.network_pallet import NetworkPalletParser
from src.main.upn.api.data_structures.network_pallet.structure import NetworkPallet


class TestNetworkPalletParser(unittest.TestCase):
    def setUp(self):
        self._parser = NetworkPalletParser()
        self._set_up_raw_network_pallet()
        self._set_up_correct_pallet()

    def _set_up_raw_network_pallet(self) -> None:
        self._raw_network_pallet = {
            'ConBarcode': 'W213359799C',
            'PalletSize': 'N',
            'PalletType': 'FULL',
            'PltBarcode': 'W213359800P'
        }

    def _set_up_correct_pallet(self) -> None:
        result = NetworkPallet()
        result.consignment_barcode_no = "W213359799C"
        result.pallet_size = "N"
        result.pallet_type = "FULL"
        result.pallet_barcode_no = "W213359800P"

        self._correct_pallet = result

    def test_should_parse_network_pallet(self):
        pallet = self._parser.parse(self._raw_network_pallet)
        self.assertEqual(self._correct_pallet, pallet)


if __name__ == '__main__':
    unittest.main()

