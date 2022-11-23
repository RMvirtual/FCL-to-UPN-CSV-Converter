import unittest
from src.test.graylaw.cargo.container import setup


class TestCargoModel(unittest.TestCase):
    def setUp(self):
        self._cargo = setup.two_entry_cargo()

    def test_should_total_weight(self) -> None:
        self.assertEqual(4200, self._cargo.total_weight)

    def test_should_get_cargo_entries(self) -> None:
        entry_1 = self._cargo[0]
        self.assertEqual(3000, entry_1.weight)
        self.assertEqual(3, entry_1.quantity)
        self.assertEqual("full", entry_1.package_type.name)

        entry_2 = self._cargo[1]
        self.assertEqual(1200, entry_2.weight)
        self.assertEqual(2, entry_2.quantity)
        self.assertEqual("half", entry_2.package_type.name)


if __name__ == "__main__":
    unittest.main()
