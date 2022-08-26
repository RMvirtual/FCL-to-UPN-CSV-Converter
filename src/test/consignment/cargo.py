import unittest
from typing import Type
from src.main.consignment.cargo.entry import CargoEntry
from src.main.consignment.cargo.types import *
from src.main.consignment.cargo.model import Cargo


class TestCargo(unittest.TestCase):
    def setUp(self) -> None:
        self._cargo = Cargo()

    def test_should_add_a_single_cargo_entry(self):
        self._create_and_add_cargo_entry(FullPallet(), (1, 1000))
        self._compare_cargo_entry(0, FullPallet, (1, 1000))

    def test_should_combine_two_cargo_entries(self):
        self._create_and_add_cargo_entry(HalfPallet(), (1, 400))
        self._create_and_add_cargo_entry(HalfPallet(), (2, 1000))

        correct_no_of_entries = 1
        correct_type = HalfPallet
        correct_qty_and__weight = (3, 1400)

        self.assertEqual(correct_no_of_entries, len(self._cargo))
        self._compare_cargo_entry(0, correct_type, correct_qty_and__weight)

    def test_should_reject_combining_two_cargo_entries(self):
        entry_1 = self._cargo_entry(HalfPallet(), (1, 400))
        entry_2 = self._cargo_entry(FullPallet(), (1, 1000))

        with self.assertRaises(ValueError):
            entry_1 += entry_2

    def test_should_reject_combining_different_oversize_entries(self):
        entry_1 = self._cargo_entry(HalfPallet(), (1, 400))
        entry_1.package_type.oversize_option = Pallet.OversizeOptions.DOUBLE

        entry_2 = self._cargo_entry(HalfPallet(), (1, 400))

        with self.assertRaises(ValueError):
            entry_1 += entry_2

    def test_should_add_two_different_pallet_types(self):
        self._create_and_add_cargo_entry(HalfPallet(), (1, 400))
        self._create_and_add_cargo_entry(FullPallet(), (3, 1000))

        correct_no_of_entries = 2

        self.assertEqual(correct_no_of_entries, len(self._cargo))
        self._compare_cargo_entry(0, HalfPallet, (1, 400))
        self._compare_cargo_entry(1, FullPallet, (3, 1000))

    def test_should_not_exceed_max_weight_when_modifying_weight(self):
        entry = self._cargo_entry(FullPallet(), (3, 3000))

        with self.assertRaises(ValueError):
            entry.weight_kgs = 4000

    def test_should_not_exceed_max_weight_when_modifying_quantity(self):
        entry = self._cargo_entry(FullPallet(), (3, 3000))

        with self.assertRaises(ValueError):
            entry.quantity = 2

    def test_should_modify_qty_and_weight(self):
        self._create_and_add_cargo_entry(FullPallet(), (1, 1000))
        self._cargo[0].quantity_and_weight = (3, 3000)

        self._compare_cargo_entry(0, FullPallet, (3, 3000))

    def test_should_not_exceed_max_weight_when_modifying_qty_and_weight(self):
        entry = self._cargo_entry(FullPallet(), (3, 3000))

        with self.assertRaises(ValueError):
            entry.quantity_and_weight = (4, 8000)

    def _create_and_add_cargo_entry(
            self, pkg_type: Pallet, qty_and_weight: tuple[int, float]) -> None:
        entry = self._cargo_entry(pkg_type, qty_and_weight)
        self._cargo.add(entry)

    @staticmethod
    def _cargo_entry(
            pkg_type: Pallet, qty_and_weight: tuple[int, float]) -> CargoEntry:
        entry = CargoEntry(pkg_type)
        entry.quantity_and_weight = qty_and_weight

        return entry

    def _compare_cargo_entry(
            self, index: int, pkg_type: Type[Pallet],
            quantity_and_weight: tuple[int, float]) -> None:

        self.assertIsInstance(self._cargo[index].package_type, pkg_type)
        self.assertEqual(quantity_and_weight[0], self._cargo[index].quantity)
        self.assertEqual(quantity_and_weight[1], self._cargo[index].weight_kgs)


if __name__ == '__main__':
    unittest.main()
