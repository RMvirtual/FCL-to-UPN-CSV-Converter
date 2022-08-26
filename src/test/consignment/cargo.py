import unittest
from src.main.consignment.cargo.entry import CargoEntry
from src.main.consignment.cargo.types import *
from src.main.consignment.cargo.model import Cargo


class TestCargo(unittest.TestCase):
    def test_should_add_a_single_cargo_entry(self):
        entry = CargoEntry(FullPallet())
        entry.quantity = 1
        entry.weight_kgs = 1000

        cargo = Cargo()
        cargo.add(entry)

        self.assertIsInstance(cargo[0].package_type, FullPallet)
        self.assertEqual(1, cargo[0].quantity)
        self.assertEqual(1000, cargo[0].weight_kgs)

    def test_should_combine_two_cargo_entries(self):
        entry_1 = CargoEntry(HalfPallet())
        entry_1.quantity = 1
        entry_1.weight_kgs = 400

        entry_2 = CargoEntry(HalfPallet())
        entry_2.quantity = 2
        entry_2.weight_kgs = 1000

        cargo = Cargo()
        cargo.add(entry_1)
        cargo.add(entry_2)

        correct_no_of_entries = 1
        correct_total_weight = 1400
        correct_total_pallets = 3

        self.assertEqual(correct_no_of_entries, len(cargo))
        self.assertEqual(correct_total_pallets, cargo[0].quantity)
        self.assertEqual(correct_total_weight, cargo[0].weight_kgs)
        self.assertIsInstance(cargo[0].package_type, HalfPallet)

    def test_should_reject_combining_two_cargo_entries(self):
        entry_1 = CargoEntry(HalfPallet())
        entry_1.quantity = 1
        entry_1.weight_kgs = 400

        entry_2 = CargoEntry(FullPallet())
        entry_2.quantity = 1
        entry_2.weight_kgs = 1000

        with self.assertRaises(ValueError):
            entry_1 += entry_2

    def test_should_add_two_different_pallet_types(self):
        entry_1 = CargoEntry(HalfPallet())
        entry_1.quantity = 1
        entry_1.weight_kgs = 400

        entry_2 = CargoEntry(FullPallet())
        entry_2.quantity = 3
        entry_2.weight_kgs = 1000

        cargo = Cargo()
        cargo.add(entry_1)
        cargo.add(entry_2)

        self.assertEqual(2, len(cargo))

        self.assertEqual(1, cargo[0].quantity)
        self.assertEqual(400, cargo[0].weight_kgs)
        self.assertIsInstance(cargo[0].package_type, HalfPallet)

        self.assertEqual(3, cargo[1].quantity)
        self.assertEqual(1000, cargo[1].weight_kgs)
        self.assertIsInstance(cargo[1].package_type, FullPallet)

    def test_should_not_exceed_max_weight_when_modifying_weight(self):
        entry = CargoEntry(FullPallet())
        entry.quantity = 3
        entry.weight_kgs = 3000

        with self.assertRaises(ValueError):
            entry.weight_kgs = 4000

    def test_should_not_exceed_max_weight_when_modifying_quantity(self):
        entry = CargoEntry(FullPallet())
        entry.quantity = 3
        entry.weight_kgs = 3000

        with self.assertRaises(ValueError):
            entry.quantity = 2

    def test_should_modify_qty_and_weight(self):
        entry = CargoEntry(FullPallet())
        entry.quantity = 1
        entry.weight_kgs = 1000

        entry.quantity_and_weight = (3, 3000)

        self.assertEqual(3, entry.quantity)
        self.assertEqual(3000, entry.weight_kgs)

    def test_should_not_exceed_max_weight_when_modifying_qty_and_weight(self):
        entry = CargoEntry(FullPallet())
        entry.quantity = 3
        entry.weight_kgs = 3000

        with self.assertRaises(ValueError):
            entry.quantity_and_weight = (4, 8000)


if __name__ == '__main__':
    unittest.main()
