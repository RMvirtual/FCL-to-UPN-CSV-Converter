import unittest
from src.main.upn.api.adaptors.network_pallet import NetworkPalletAdaptor
from src.test.upn.api.adaptors.network_pallet import setup


class TestNetworkPalletMapping(unittest.TestCase):
    def setUp(self):
        self._full_normal_pallet = NetworkPalletAdaptor(
            setup.full_normal_pallet())

        self._double_half_pallet = NetworkPalletAdaptor(
            setup.double_half_pallet())

    def test_should_adapt_base_type(self) -> None:
        self.assertEqual("pallet", self._full_normal_pallet.base_type)

    def test_should_adapt_name(self) -> None:
        self.assertEqual("full", self._full_normal_pallet.name)

    def test_should_adapt_oversize_values(self) -> None:
        self.fail("DUMMY FAIL")

    def test_should_adapt_maximum_dimensions(self) -> None:
        self.assertEqual(
            setup.full_normal_max_dims(),
            self._full_normal_pallet.maximum_dimensions
        )

        self.assertEqual(
            setup.double_half_max_dims(),
            self._double_half_pallet.maximum_dimensions
        )

    def test_should_adapt_maximum_weight(self) -> None:
        self.assertEqual(1200, self._full_normal_pallet.maximum_weight)
        self.assertEqual(600, self._double_half_pallet.maximum_weight)

    def test_should_adapt_override_options(self) -> None:
        self.assertListEqual([], self._full_normal_pallet.override_options)


if __name__ == '__main__':
    unittest.main()
