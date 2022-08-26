import unittest
from src.main.consignment.cargo.entry import CargoEntry
from src.main.consignment.cargo.types import *
from src.main.consignment.cargo.model import Cargo


class TestCargo(unittest.TestCase):
    def setUp(self) -> None:
        self._cargo = Cargo()

    def test_should_add_a_single_cargo_entry(self):
        entry = self._cargo_entry(FullPallet(), (1, 1000))
        self._cargo.add(entry)

        self.assertIsInstance(self._cargo[0].package_type, FullPallet)
        self.assertEqual(1, self._cargo[0].quantity)
        self.assertEqual(1000, self._cargo[0].weight_kgs)

    def test_should_combine_two_cargo_entries(self):
        entry_1 = self._cargo_entry(HalfPallet(), (1, 400))
        entry_2 = self._cargo_entry(HalfPallet(), (2, 1000))

        self._cargo.add(entry_1)
        self._cargo.add(entry_2)

        correct_no_of_entries = 1
        correct_total_weight = 1400
        correct_total_pallets = 3

        self.assertEqual(correct_no_of_entries, len(self._cargo))
        self.assertEqual(correct_total_pallets, self._cargo[0].quantity)
        self.assertEqual(correct_total_weight, self._cargo[0].weight_kgs)
        self.assertIsInstance(self._cargo[0].package_type, HalfPallet)

    def test_should_reject_combining_two_cargo_entries(self):
        entry_1 = self._cargo_entry(HalfPallet(), (1, 400))
        entry_2 = self._cargo_entry(FullPallet(), (1, 1000))

        with self.assertRaises(ValueError):
            entry_1 += entry_2

    def test_should_add_two_different_pallet_types(self):
        entry_1 = self._cargo_entry(HalfPallet(), (1, 400))
        entry_2 = self._cargo_entry(FullPallet(), (3, 1000))
        self._cargo.add(entry_1)
        self._cargo.add(entry_2)

        self.assertEqual(2, len(self._cargo))

        self.assertEqual(1, self._cargo[0].quantity)
        self.assertEqual(400, self._cargo[0].weight_kgs)
        self.assertIsInstance(self._cargo[0].package_type, HalfPallet)

        self.assertEqual(3, self._cargo[1].quantity)
        self.assertEqual(1000, self._cargo[1].weight_kgs)
        self.assertIsInstance(self._cargo[1].package_type, FullPallet)

    def test_should_not_exceed_max_weight_when_modifying_weight(self):
        entry = self._cargo_entry(FullPallet(), (3, 3000))

        with self.assertRaises(ValueError):
            entry.weight_kgs = 4000

    def test_should_not_exceed_max_weight_when_modifying_quantity(self):
        entry = self._cargo_entry(FullPallet(), (3, 3000))

        with self.assertRaises(ValueError):
            entry.quantity = 2

    def test_should_modify_qty_and_weight(self):
        entry = self._cargo_entry(FullPallet(), (1, 1000))
        entry.quantity_and_weight = (3, 3000)

        self.assertEqual(3, entry.quantity)
        self.assertEqual(3000, entry.weight_kgs)

    def test_should_not_exceed_max_weight_when_modifying_qty_and_weight(self):
        entry = self._cargo_entry(FullPallet(), (3, 3000))

        with self.assertRaises(ValueError):
            entry.quantity_and_weight = (4, 8000)

    @staticmethod
    def _cargo_entry(
            pkg_type: Pallet, qty_and_weight: tuple[int, float]) -> CargoEntry:
        entry = CargoEntry(pkg_type)
        entry.quantity_and_weight = qty_and_weight

        return entry


if __name__ == '__main__':
    unittest.main()
