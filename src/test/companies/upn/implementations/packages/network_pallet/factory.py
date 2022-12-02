import unittest
from src.main.companies.upn.implementations.packages.network_pallet import (
    factory)


class TestNetworkPalletFactory(unittest.TestCase):
    def test_should_set_type(self):
        pallet = factory.network_pallet("FULL", "N")
        self.assertEqual("FULL", pallet.type)
        self.assertEqual("N", pallet.size)


if __name__ == '__main__':
    unittest.main()
