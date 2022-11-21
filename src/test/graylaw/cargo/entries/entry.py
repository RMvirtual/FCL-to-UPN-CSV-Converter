import unittest
from src.test.graylaw.cargo.entries.setup.packages import DummyPallets
from src.test.graylaw.cargo.entries.setup import cargo_entries
from src.test.graylaw.cargo.entries import assertions


class TestCargoEntry(unittest.TestCase):
    def setUp(self) -> None:
        self._pallets = DummyPallets()

    def test_should_combine_two_cargo_entries(self):
        entry_1 = cargo_entries.half_pallet_entry(1, 400)
        entry_2 = cargo_entries.half_pallet_entry(2, 1000)

        entry_1 += entry_2

        assertions.compare_cargo_entry(
            tester=self,
            cargo_entry=entry_1,
            pkg_type=self._pallets.half,
            quantity_and_weight=(3, 1400)
        )

    def test_should_reject_combining_two_cargo_entries(self):
        with self.assertRaises(ValueError):
            entry_1 = cargo_entries.half_pallet_entry(1, 400)
            entry_2 = cargo_entries.full_pallet_entry(1, 1000)

            entry_1 += entry_2

    def test_should_combine_entries_of_special_oversize(self):
        entry_1 = cargo_entries.half_pallet_entry(1, 400, "double")
        entry_2 = cargo_entries.half_pallet_entry(2, 300, "double")

        entry_1 += entry_2

        assertions.compare_cargo_entry(
            tester=self, cargo_entry=entry_1, pkg_type=self._pallets.half,
            quantity_and_weight=(3, 700), oversize_option="double"
        )

    def test_should_reject_combining_different_oversize_entries(self):
        entry_1 = cargo_entries.half_pallet_entry(1, 400, "triple")
        entry_2 = cargo_entries.half_pallet_entry(1, 400, "double")

        with self.assertRaises(ValueError):
            entry_1 += entry_2

    def test_should_not_exceed_max_weight_when_modifying_weight(self):
        with self.assertRaises(ValueError):
            entry = cargo_entries.full_pallet_entry(3, 3000)
            entry.weight = 4000

    def test_should_not_exceed_max_weight_when_modifying_quantity(self):
        with self.assertRaises(ValueError):
            entry = cargo_entries.full_pallet_entry(3, 3000)
            entry.quantity = 2

    def test_should_modify_qty_and_weight(self):
        entry = cargo_entries.full_pallet_entry(1, 1000)
        entry.set_totals(quantity=3, weight=3000)

        assertions.compare_cargo_entry(
            tester=self,
            cargo_entry=entry,
            pkg_type=self._pallets.full,
            quantity_and_weight=(3, 3000)
        )

    def test_should_not_exceed_max_weight_when_modifying_qty_and_weight(self):
        with self.assertRaises(ValueError):
            entry = cargo_entries.full_pallet_entry(3, 3000)
            entry.set_totals(quantity=4, weight=8000)


if __name__ == '__main__':
    unittest.main()
