import unittest
from src.main.companies.upn.api.implementation_1.api.pallets.download import \
    factory


class TestNetworkPalletFactory(unittest.TestCase):
    def test_should_set_type(self):
        pallet = factory.network_pallet("FULL", "N")
        self.assertEqual("FULL", pallet.type)
        self.assertEqual("N", pallet.size)


if __name__ == '__main__':
    unittest.main()
