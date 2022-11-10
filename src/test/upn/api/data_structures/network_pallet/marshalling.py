import unittest
from src.main.upn.api.data_structures.network_pallet.structure \
    import NetworkPallet

from src.main.upn.api.data_structures.network_pallet.marshalling \
    import UpnNetworkPalletMarshaller


class TestNetworkPalletMarshaller(unittest.TestCase):
    def setUp(self) -> None:
        self._marshaller = UpnNetworkPalletMarshaller()
        self._set_up_marshalled_pallet()
        self._set_up_correct_unmarshalled_pallet()

    def _set_up_marshalled_pallet(self) -> None:
        self._unmarshall_candidate = {
            'ConBarcode': 'W213359799C',
            'PalletSize': 'N',
            'PalletType': 'FULL',
            'PltBarcode': 'W213359800P'
        }

    def _set_up_correct_unmarshalled_pallet(self) -> None:
        result = NetworkPallet()
        result.consignment_barcode_no = "W213359799C"
        result.pallet_size = "N"
        result.pallet_type = "FULL"
        result.pallet_barcode_no = "W213359800P"

        self._correct_pallet = result

    def test_should_unmarshall_network_pallet(self):
        result = self._marshaller.unmarshall(self._unmarshall_candidate)

        received_to_correct_results = list({
            result.consignment_barcode_no:
                self._correct_pallet.consignment_barcode_no,
            result.pallet_size: self._correct_pallet.pallet_size,
            result.pallet_type: self._correct_pallet.type,
            result.pallet_barcode_no: self._correct_pallet.pallet_barcode_no
        }.items())

        for result, correct_result in received_to_correct_results:
            self.assertEqual(correct_result, result)


if __name__ == '__main__':
    unittest.main()
