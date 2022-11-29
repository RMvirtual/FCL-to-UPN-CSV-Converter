import unittest
from src.main.freight.cargo.entries import factory
from src.main.freight.cargo.entries.validation import CargoEntryException


class TestCargoEntry(unittest.TestCase):
    def test_should_combine_two_cargo_entries(self):
        entry = factory.half_pallet_entry(1, 400)
        other_entry = factory.half_pallet_entry(2, 1000)
        entry += other_entry

        self.assertEqual(1400, entry.weight)
        self.assertEqual(3, entry.quantity)
        self.assertEqual("half", entry.package_type.name)
        self.assertEqual("normal", entry.package_type.oversize.selected.name)

    def test_should_combine_entries_of_special_oversize(self):
        entry = factory.half_pallet_entry(1, 400, "double")
        other_entry = factory.half_pallet_entry(2, 300, "double")
        entry += other_entry

        self.assertEqual(700, entry.weight)
        self.assertEqual(3, entry.quantity)
        self.assertEqual("half", entry.package_type.name)
        self.assertEqual("double", entry.package_type.oversize.selected.name)

    def test_should_modify_qty_and_weight(self):
        entry = factory.full_pallet_entry(1, 1000)
        entry.set_totals(quantity=3, weight=3000)

        self.assertEqual(3000, entry.weight)
        self.assertEqual(3, entry.quantity)
        self.assertEqual("full", entry.package_type.name)
        self.assertEqual("normal", entry.package_type.oversize.selected.name)

    def test_should_not_exceed_max_weight_when_modifying_qty_and_weight(self):
        with self.assertRaises(CargoEntryException):
            entry = factory.full_pallet_entry(3, 3000)
            entry.set_totals(quantity=4, weight=8000)

    def test_should_reject_combining_two_cargo_entries(self):
        with self.assertRaises(CargoEntryException):
            entry_1 = factory.half_pallet_entry(1, 400)
            entry_2 = factory.full_pallet_entry(1, 1000)

            entry_1 += entry_2

    def test_should_not_exceed_max_weight_when_modifying_quantity(self):
        with self.assertRaises(CargoEntryException):
            entry = factory.full_pallet_entry(3, 3000)
            entry.quantity = 2

    def test_should_not_exceed_max_weight_when_modifying_weight(self):
        with self.assertRaises(CargoEntryException):
            entry = factory.full_pallet_entry(3, 3000)
            entry.weight = 4000

    def test_should_reject_combining_different_oversize_entries(self):
        with self.assertRaises(CargoEntryException):
            entry = factory.half_pallet_entry(1, 400, "triple")
            other_entry = factory.half_pallet_entry(1, 400, "double")
            entry += other_entry


if __name__ == '__main__':
    unittest.main()
