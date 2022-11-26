import unittest
from src.main.graylaw.packages.types import database


class TestGraylawPackageTypeDatabase(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_should_get_base_type_from_full_pallet(self):
        package_type = database.load("full")
        self.assertEqual(package_type.base_type, "pallet")

    def test_should_show_identical_normal_package_types_as_equal(self):
        package_1 = database.load("full")
        package_2 = database.load("full")

        self.assertTrue(package_1 == package_2)
        self.assertFalse(package_1 != package_2)

    def test_should_show_identical_oversize_package_types_as_equal(self):
        package_1 = database.load("full")
        package_2 = database.load("full")

        package_1.oversize.select("double")
        package_2.oversize.select("double")

        self.assertTrue(package_1 == package_2)
        self.assertFalse(package_1 != package_2)

    def test_should_show_different_normal_package_types_as_inequal(self):
        package_1 = database.load("full")
        package_2 = database.load("half")

        self.assertTrue(package_1 != package_2)
        self.assertFalse(package_1 == package_2)

    def test_should_show_different_oversize_package_types_as_inequal(self):
        package_1 = database.load("full")
        package_2 = database.load("full")

        package_1.oversize.selected = package_1.oversize["double"]
        package_2.oversize.selected = package_2.oversize["triple"]

        self.assertTrue(package_1 != package_2)
        self.assertFalse(package_1 == package_2)


if __name__ == '__main__':
    unittest.main()
