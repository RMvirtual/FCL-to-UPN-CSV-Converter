import unittest
from src.main.freight.cargo.entry import CargoEntry
from src.main.freight.cargo.packages.package_types import load, PackageType


class TestCargoEntry(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_should_create_a_single_cargo_entry(self):
        package_type = load("full")
        entry = self._cargo_entry(package_type, (1, 1000))

        self._compare_cargo_entry(
            cargo_entry=entry,
            pkg_type=package_type,
            quantity_and_weight=(1, 1000)
        )

    def test_should_combine_two_cargo_entries(self):
        package_type = load("half")
        entry_1 = self._cargo_entry(package_type, (1, 400))
        entry_2 = self._cargo_entry(package_type, (2, 1000))

        entry_1 += entry_2

        self._compare_cargo_entry(
            cargo_entry=entry_1,
            pkg_type=package_type,
            quantity_and_weight=(3, 1400)
        )

    def test_should_reject_combining_two_cargo_entries(self):
        half_pallet = load("half")
        full_pallet = load("full")
        entry_1 = self._cargo_entry(half_pallet, (1, 400))
        entry_2 = self._cargo_entry(full_pallet, (1, 1000))

        with self.assertRaises(ValueError):
            entry_1 += entry_2

    def test_should_reject_combining_different_oversize_entries(self):
        half_pallet = load("half")

        entry_1 = self._cargo_entry(half_pallet, (1, 400))
        entry_2 = self._cargo_entry(half_pallet, (1, 400))

        entry_1.package_type.oversize_option = "double"
        entry_2.package_type.oversize_option = "triple"

        with self.assertRaises(ValueError):
            entry_1 += entry_2

    def test_should_combine_entries_of_special_oversize(self):
        half_pallet = load("half")

        entry_1 = self._cargo_entry(half_pallet, (1, 400), "double")
        entry_2 = self._cargo_entry(half_pallet, (2, 300), "double")

        entry_1 += entry_2

        self._compare_cargo_entry(
            cargo_entry=entry_1,
            pkg_type=half_pallet,
            quantity_and_weight=(3, 700),
            oversize_option="double"
        )

    def test_should_not_exceed_max_weight_when_modifying_weight(self):
        full_pallet = load("full")
        entry = self._cargo_entry(full_pallet, (3, 3000))

        with self.assertRaises(ValueError):
            entry.weight_kgs = 4000

    def test_should_not_exceed_max_weight_when_modifying_quantity(self):
        full_pallet = load("full")
        entry = self._cargo_entry(full_pallet, (3, 3000))

        with self.assertRaises(ValueError):
            entry.quantity = 2

    def test_should_modify_qty_and_weight(self):
        full_pallet = load("full")
        entry = self._cargo_entry(full_pallet, (1, 1000))
        entry.quantity_and_weight = (3, 3000)

        self._compare_cargo_entry(
            cargo_entry=entry,
            pkg_type=full_pallet,
            quantity_and_weight=(3, 3000)
        )

    def test_should_not_exceed_max_weight_when_modifying_qty_and_weight(self):
        full_pallet = load("full")
        entry = self._cargo_entry(full_pallet, (3, 3000))

        with self.assertRaises(ValueError):
            entry.quantity_and_weight = (4, 8000)

    @staticmethod
    def _cargo_entry(
            pkg_type: PackageType, qty_and_weight: tuple[int, float],
            oversize_option: str = None
    ) -> CargoEntry:
        result = CargoEntry(pkg_type)
        result.quantity_and_weight = qty_and_weight

        if oversize_option:
            result.package_type.oversize_option = oversize_option

        return result

    def _compare_cargo_entry(
            self, cargo_entry: CargoEntry, pkg_type: PackageType,
            quantity_and_weight: tuple[int, float],
            oversize_option: dict[str, float] = None
    ) -> None:
        self.assertEqual(quantity_and_weight[0], cargo_entry.quantity)
        self.assertEqual(quantity_and_weight[1], cargo_entry.weight_kgs)
        self.compare_cargo_entry_package_type(cargo_entry, pkg_type)

        if oversize_option:
            self.assertEqual(
                cargo_entry.package_type.oversize_option, oversize_option)

    def compare_cargo_entry_package_type(
            self, cargo_entry: CargoEntry, pkg_type: PackageType) -> None:
        cargo_package_type = cargo_entry.package_type

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
