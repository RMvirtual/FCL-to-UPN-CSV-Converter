import unittest
from src.main.companies.upn.database.pallets import UPNPalletsDatabase


class TestUPNPalletDatabase(unittest.TestCase):
    def setUp(self):
        self._database = UPNPalletsDatabase()

    def test_should_get_network_pallet(self) -> None:
        result = self._database.network_pallet()

        self.assertEqual("FULL", result.type)
        self.assertEqual("NORMAL", result.size)
        self.assertListEqual(
            ["FULL", "HALF", "EURO", "QUARTER", "MICRO"],
            result.type_constraints
        )

        self.assertListEqual(["N", "O", "2", "3"], result.size_constraints)


if __name__ == '__main__':
    unittest.main()
