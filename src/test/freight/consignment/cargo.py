import unittest
from typing import Type
from src.main.consignment.cargo.entry import CargoEntry
from src.main.consignment.cargo.types import *
from src.main.consignment.cargo.model import Cargo


class TestCargo(unittest.TestCase):
    def setUp(self) -> None:
        self._cargo = Cargo()

    def test_should_add_a_single_cargo_entry(self):
        self._add_cargo_entry(FullPallet(), (1, 1000))

        self._compare_cargo_entry(
            index=0, pkg_type=FullPallet, quantity_and_weight=(1, 1000))

    def test_should_combine_two_cargo_entries(self):
        self._add_cargo_entry(HalfPallet(), (1, 400))
        self._add_cargo_entry(HalfPallet(), (2, 1000))

        correct_size = 1
        self.assertEqual(correct_size, len(self._cargo))

        self._compare_cargo_entry(
            index=0, pkg_type=HalfPallet, quantity_and_weight=(3, 1400))

    def test_should_reject_combining_two_cargo_entries(self):
        entry_1 = self._cargo_entry(HalfPallet(), (1, 400))
        entry_2 = self._cargo_entry(FullPallet(), (1, 1000))

        with self.assertRaises(ValueError):
            entry_1 += entry_2

    def test_should_reject_combining_different_oversize_entries(self):
        entry_1 = self._cargo_entry(HalfPallet(), (1, 400))
        entry_1.package_type.oversize_option = OversizeOptions.DOUBLE

        entry_2 = self._cargo_entry(HalfPallet(), (1, 400))

        with self.assertRaises(ValueError):
            entry_1 += entry_2

    def test_should_combine_entries_of_special_oversize(self):
        self._add_cargo_entry(
            HalfPallet(), (1, 400), OversizeOptions.DOUBLE)

        self._add_cargo_entry(
            HalfPallet(), (2, 300), OversizeOptions.DOUBLE)

        self._compare_cargo_entry(
            index=0,
            pkg_type=HalfPallet,
            quantity_and_weight=(3, 700),
            oversize_option=OversizeOptions.DOUBLE
        )

    def test_should_add_two_different_pallet_types(self):
        self._add_cargo_entry(HalfPallet(), (1, 400))
        self._add_cargo_entry(FullPallet(), (3, 1000))

        correct_size = 2
        self.assertEqual(correct_size, len(self._cargo))

        self._compare_cargo_entry(
            index=0, pkg_type=HalfPallet, quantity_and_weight=(1, 400))

        self._compare_cargo_entry(
            index=1, pkg_type=FullPallet, quantity_and_weight=(3, 1000))

    def test_should_not_exceed_max_weight_when_modifying_weight(self):
        entry = self._cargo_entry(FullPallet(), (3, 3000))

        with self.assertRaises(ValueError):
            entry.weight_kgs = 4000

    def test_should_not_exceed_max_weight_when_modifying_quantity(self):
        entry = self._cargo_entry(FullPallet(), (3, 3000))

        with self.assertRaises(ValueError):
            entry.quantity = 2

    def test_should_modify_qty_and_weight(self):
        self._add_cargo_entry(FullPallet(), (1, 1000))
        self._cargo[0].quantity_and_weight = (3, 3000)

        self._compare_cargo_entry(
            index=0, pkg_type=FullPallet, quantity_and_weight=(3, 3000))

    def test_should_not_exceed_max_weight_when_modifying_qty_and_weight(self):
        entry = self._cargo_entry(FullPallet(), (3, 3000))

        with self.assertRaises(ValueError):
            entry.quantity_and_weight = (4, 8000)

    def _add_cargo_entry(
            self, pkg_type: Pallet, qty_and_weight: tuple[int, float],
            oversize_option: OversizeOptions = None
    ) -> None:
        entry = self._cargo_entry(pkg_type, qty_and_weight, oversize_option)

        self._cargo.add(entry)

    @staticmethod
    def _cargo_entry(
            pkg_type: Pallet, qty_and_weight: tuple[int, float],
            oversize_option: OversizeOptions = None
    ) -> CargoEntry:
        entry = CargoEntry(pkg_type)
        entry.quantity_and_weight = qty_and_weight

        if oversize_option:
            entry.package_type.oversize_option = oversize_option

        return entry

    def _compare_cargo_entry(
            self, index: int, pkg_type: Type[Pallet],
            quantity_and_weight: tuple[int, float],
            oversize_option: OversizeOptions = None
    ) -> None:
        self.assertIsInstance(self._cargo[index].package_type, pkg_type)
        self.assertEqual(quantity_and_weight[0], self._cargo[index].quantity)
        self.assertEqual(quantity_and_weight[1], self._cargo[index].weight_kgs)

        if oversize_option:
            self.assertEqual(
                self._cargo[index].package_type.oversize_option,
                oversize_option
            )


if __name__ == '__main__':
    unittest.main()
