import unittest
from src.main.graylaw.cargo.packages.types import factory
from src.main.upn.api.adaptors.network_pallet import NetworkPalletAdaptor
from src.test.upn.api.adaptors.network_pallet import setup


class TestNetworkPalletMapping(unittest.TestCase):
    def setUp(self):
        self._correct_pallet = factory.load("full")
        self._adaptor = NetworkPalletAdaptor(setup.network_pallet())

    def test_should_return_base_type(self) -> None:
        self.assertEqual("pallet", self._adaptor.base_type)

    def test_should_return_name(self) -> None:
        self.assertEqual("full", self._adaptor.name)


if __name__ == '__main__':
    unittest.main()
