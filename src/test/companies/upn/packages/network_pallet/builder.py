import unittest
from src.main.companies.upn.packages.network_pallet.builder import NetworkPalletBuilder


class TestUPNNetworkPallet(unittest.TestCase):
    def setUp(self):
        pass

    def test_should_build_network_pallet(self) -> None:
        builder = NetworkPalletBuilder()
        builder.set_type("FULL")
        builder.set_size("N")
        builder.set_barcode("W123465789")
        builder.set_consignment_barcode("W987654321")
        builder.set_type_constraints(["FULL", "HALF"])
        builder.set_size_constraints(["N", "O", "2", "3"])
        pallet = builder.build()

        self.assertEqual("FULL", pallet.type)
        self.assertEqual("N", pallet.size)
        self.assertEqual("W123465789", pallet.barcode)
        self.assertEqual("W987654321", pallet.consignment_barcode)


if __name__ == '__main__':
    unittest.main()
