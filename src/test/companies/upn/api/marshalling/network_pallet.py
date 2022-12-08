import unittest
from src.main.companies.upn.api.marshalling.api.network_pallet \
    import UpnNetworkPalletMarshaller


class TestNetworkPalletMarshaller(unittest.TestCase):
    def setUp(self) -> None:
        self._marshaller = UpnNetworkPalletMarshaller()
        self._set_up_marshalled_pallet()

    def _set_up_marshalled_pallet(self) -> None:
        self._unmarshall_candidate = {
            'ConBarcode': 'W213359799C',
            'PalletSize': 'N',
            'PalletType': 'FULL',
            'PltBarcode': 'W213359800P'
        }

    def test_should_unmarshall_network_pallet(self):
        pallet = self._marshaller.unmarshall(self._unmarshall_candidate)

        self.assertEqual("FULL", pallet.type)
        self.assertEqual("N", pallet.size)
        self.assertEqual("W213359800P", pallet.barcode)
        self.assertEqual("W213359799C", pallet.consignment_barcode)


if __name__ == '__main__':
    unittest.main()
