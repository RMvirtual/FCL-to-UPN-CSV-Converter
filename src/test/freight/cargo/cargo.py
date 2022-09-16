import unittest
from src.main.freight.cargo.entry import CargoEntry
from src.main.freight.cargo.types import load_package_type, PackageType
from src.main.freight.cargo.model import Cargo


class TestCargo(unittest.TestCase):
    def setUp(self) -> None:
        self._cargo = Cargo()

    def test_should_add_a_single_cargo_entry(self):
        package_type = load_package_type("full")
        self._add_cargo_entry(package_type, (1, 1000))

        self._compare_cargo_entry(
            index=0, pkg_type=package_type, quantity_and_weight=(1, 1000))

    def test_should_combine_two_cargo_entries(self):
        package_type = load_package_type("half")
        self._add_cargo_entry(package_type, (1, 400))
        self._add_cargo_entry(package_type, (2, 1000))

        correct_size = 1
        self.assertEqual(correct_size, len(self._cargo))

        self._compare_cargo_entry(
            index=0, pkg_type=package_type, quantity_and_weight=(3, 1400))

    def test_should_reject_combining_two_cargo_entries(self):
        half_pallet = load_package_type("half")
        full_pallet = load_package_type("full")
        entry_1 = self._cargo_entry(half_pallet, (1, 400))
        entry_2 = self._cargo_entry(full_pallet, (1, 1000))

        with self.assertRaises(ValueError):
            entry_1 += entry_2

    def test_should_reject_combining_different_oversize_entries(self):
        half_pallet = load_package_type("half")
        entry_1 = self._cargo_entry(half_pallet, (1, 400))
        entry_1.package_type.oversize_option = "double"

        entry_2 = self._cargo_entry(half_pallet, (1, 400))

        with self.assertRaises(ValueError):
            entry_1 += entry_2

    def test_should_combine_entries_of_special_oversize(self):
        half_pallet = load_package_type("half")

        self._add_cargo_entry(
            half_pallet, (1, 400), "double")

        self._add_cargo_entry(
            half_pallet, (2, 300), "double")

        self._compare_cargo_entry(
            index=0,
            pkg_type=half_pallet,
            quantity_and_weight=(3, 700),
            oversize_option="double"
        )

    def test_should_add_two_different_pallet_types(self):
        half_pallet = load_package_type("half")
        full_pallet = load_package_type("full")

        self._add_cargo_entry(half_pallet, (1, 400))
        self._add_cargo_entry(full_pallet, (3, 1000))

        correct_size = 2
        self.assertEqual(correct_size, len(self._cargo))

        self._compare_cargo_entry(
            index=0, pkg_type=half_pallet, quantity_and_weight=(1, 400))

        self._compare_cargo_entry(
            index=1, pkg_type=full_pallet, quantity_and_weight=(3, 1000))

    def test_should_not_exceed_max_weight_when_modifying_weight(self):
        full_pallet = load_package_type("full")
        entry = self._cargo_entry(full_pallet, (3, 3000))

        with self.assertRaises(ValueError):
            entry.weight_kgs = 4000

    def test_should_not_exceed_max_weight_when_modifying_quantity(self):
        full_pallet = load_package_type("full")
        entry = self._cargo_entry(full_pallet, (3, 3000))

        with self.assertRaises(ValueError):
            entry.quantity = 2

    def test_should_modify_qty_and_weight(self):
        full_pallet = load_package_type("full")
        self._add_cargo_entry(full_pallet, (1, 1000))
        self._cargo[0].quantity_and_weight = (3, 3000)

        self._compare_cargo_entry(
            index=0, pkg_type=full_pallet, quantity_and_weight=(3, 3000))

    def test_should_not_exceed_max_weight_when_modifying_qty_and_weight(self):
        full_pallet = load_package_type("full")
        entry = self._cargo_entry(full_pallet, (3, 3000))

        with self.assertRaises(ValueError):
            entry.quantity_and_weight = (4, 8000)

    def _add_cargo_entry(
            self, pkg_type: PackageType, qty_and_weight: tuple[int, float],
            oversize_option: dict[str, float] = None
    ) -> None:
        entry = self._cargo_entry(pkg_type, qty_and_weight, oversize_option)

        self._cargo.add(entry)

    @staticmethod
    def _cargo_entry(
            pkg_type: PackageType, qty_and_weight: tuple[int, float],
            oversize_option: dict[str, float] = None
    ) -> CargoEntry:
        entry = CargoEntry(pkg_type)
        entry.quantity_and_weight = qty_and_weight

        if oversize_option:
            entry.package_type.oversize_option = oversize_option

        return entry

    def _compare_cargo_entry(
            self, index: int, pkg_type: PackageType,
            quantity_and_weight: tuple[int, float],
            oversize_option: dict[str, float] = None
    ) -> None:
        self.assertEqual(quantity_and_weight[0], self._cargo[index].quantity)
        self.assertEqual(quantity_and_weight[1], self._cargo[index].weight_kgs)
        self.compare_cargo_entry_package_type(index, pkg_type)

        if oversize_option:
            self.assertEqual(
                self._cargo[index].package_type.oversize_option,
                oversize_option
            )

    def compare_cargo_entry_package_type(
            self, index: int, pkg_type: PackageType) -> None:
        cargo_package_type = self._cargo[index].package_type

        self.assertEqual(pkg_type.base_type, cargo_package_type.base_type)
        self.assertEqual(pkg_type.name, cargo_package_type.name)

        self.assertEqual(
            pkg_type.maximum_weight, cargo_package_type.maximum_weight)

        self.assertDictEqual(
            pkg_type.maximum_dimensions, cargo_package_type.maximum_dimensions)

        self.assertListEqual(
            pkg_type.override_options, cargo_package_type.override_options)

    def compare_oversize_option(
            self, pkg_type_1: PackageType, pkg_type_2: PackageType) -> None:
        self.assertDictEqual(
            pkg_type_1.oversize_option,
            pkg_type_2.oversize_option
        )


if __name__ == '__main__':
    unittest.main()
