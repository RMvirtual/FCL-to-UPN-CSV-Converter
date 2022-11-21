import unittest
from src.main.upn.api.adaptors.network_pallet import NetworkPalletAdaptor
from src.test.upn.api.adaptors.network_pallet import setup


class TestNetworkPalletMapping(unittest.TestCase):
    def setUp(self):
        self._normal_full_pallet = NetworkPalletAdaptor(
            setup.full_normal_pallet())

        self._double_half_pallet_adaptor = NetworkPalletAdaptor(
            setup.double_half_pallet())

    def test_should_adapt_base_type(self) -> None:
        self.assertEqual("pallet", self._normal_full_pallet.base_type)

    def test_should_adapt_name(self) -> None:
        self.assertEqual("full", self._normal_full_pallet.name)

    def test_should_adapt_oversize_values(self) -> None:
        self.fail("DUMMY FAIL")

    def test_should_adapt_maximum_dimensions(self) -> None:
        self.fail("DUMMY FAIL")

    def test_should_adapt_maximum_weight(self) -> None:
        self.assertEqual(1200, self._normal_full_pallet.maximum_weight)
        self.assertEqual(600, self._double_half_pallet_adaptor.maximum_weight)

    def test_should_adapt_override_options(self) -> None:
        self.assertListEqual([], self._normal_full_pallet.override_options)


if __name__ == '__main__':
    unittest.main()
