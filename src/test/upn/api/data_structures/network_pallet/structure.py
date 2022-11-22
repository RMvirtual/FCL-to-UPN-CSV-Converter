import unittest
from src.main.upn.api.data_structures.network_pallet.implementation \
    import NetworkPallet


class TestNetworkPalletStructure(unittest.TestCase):
    def setUp(self):
        self._pallet = NetworkPallet()

    def test_should_set_type(self):
        self._pallet.type = "FULL"
        self.assertEqual("FULL", self._pallet.type)

        self._pallet.type = "MICRO"
        self.assertEqual("MICRO", self._pallet.type)


if __name__ == '__main__':
    unittest.main()
