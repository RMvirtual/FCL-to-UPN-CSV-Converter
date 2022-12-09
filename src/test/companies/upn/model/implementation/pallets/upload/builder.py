import unittest
from src.main.companies.upn.api.implementation_1.api.pallets.upload.builder \
    import CustPalletBuilder


class TestUPNCustPalletBuilder(unittest.TestCase):
    def setUp(self):
        pass

    def test_should_build_cust_pallet(self) -> None:
        builder = CustPalletBuilder()
        builder.set_type("FULL")
        builder.set_size("N")
        builder.set_type_constraints(["FULL", "HALF"])
        builder.set_size_constraints(["N", "O", "2", "3"])
        builder.set_weight(600)
        pallet = builder.build()

        self.assertEqual("FULL", pallet.type)
        self.assertEqual("N", pallet.size)
        self.assertEqual(600, pallet.weight)


if __name__ == '__main__':
    unittest.main()
