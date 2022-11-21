import unittest
from src.main.freight.cargo.packages.types import factory

from src.main.upn.api.data_structures.network_pallet.structure \
    import NetworkPallet

from src.main.upn.api.mapping.network_pallet import NetworkPalletAdapter


class TestNetworkPalletMapping(unittest.TestCase):
    def setUp(self):
        self._network_pallet = self._set_up_network_pallet()
        self._correct_pallet = factory.load("full")

    @staticmethod
    def _set_up_network_pallet() -> NetworkPallet:
        result = NetworkPallet()
        result.consignment_barcode = "W213359799C"
        result.pallet_size = "N"
        result.pallet_type = "FULL"
        result.barcode = "W213359800P"

        return result

    def test_should_convert_network_pallet_into_house_pallet(self) -> None:
        result = NetworkPalletAdapter(self._network_pallet)


if __name__ == '__main__':
    unittest.main()
