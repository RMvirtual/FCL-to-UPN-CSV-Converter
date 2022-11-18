from unittest import TestCase
from src.main.freight.cargo.entries.entry import CargoEntry
from src.main.freight.cargo.packages.types.interface import PackageType


def compare_cargo_entry(
        tester: TestCase, cargo_entry: CargoEntry, pkg_type: PackageType,
        quantity_and_weight: tuple[int, float],
        oversize_option: dict[str, float] = None
) -> None:
    tester.assertEqual(quantity_and_weight[0], cargo_entry.quantity)
    tester.assertEqual(quantity_and_weight[1], cargo_entry.weight_kgs)
    compare_cargo_entry_to_package_type(tester, cargo_entry, pkg_type)

    if oversize_option:
        tester.assertEqual(
            cargo_entry.package_type.oversize.selected.name, oversize_option)


def compare_cargo_entry_to_package_type(
        tester: TestCase, cargo_entry: CargoEntry, package_type: PackageType
) -> None:
    package_2 = cargo_entry.package_type

    tester.assertEqual(package_type.base_type, package_2.base_type)
    tester.assertEqual(package_type.name, package_2.name)
    tester.assertEqual(package_type.maximum_weight, package_2.maximum_weight)

    tester.assertEqual(
        package_type.maximum_dimensions, package_2.maximum_dimensions)

    tester.assertListEqual(
        package_type.override_options, package_2.override_options)


def compare_oversize(
        tester: TestCase, package_1: PackageType, package_2: PackageType
) -> None:
    tester.assertEqual(
        package_1.oversize.selected, package_2.oversize.selected)
