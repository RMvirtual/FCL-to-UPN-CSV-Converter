import unittest
from src.main.graylaw.cargo.packages.types import factory
from src.test.graylaw.cargo.packages.types.builder import setup


class TestPackageTypeBuilder(unittest.TestCase):
    def setUp(self) -> None:
        self._double_half = setup._double_half_pallet()

    def test_should_get_base_type_from_full_pallet(self):
        package_type = factory.load("full")
        self.assertEqual(package_type.base_type, "pallet")

    def test_should_show_identical_normal_package_types_as_equal(self):
        package_1 = factory.load("full")
        package_2 = factory.load("full")

        self.assertTrue(package_1 == package_2)
        self.assertFalse(package_1 != package_2)

    def test_should_show_identical_oversize_package_types_as_equal(self):
        package_1 = factory.load("full")
        package_2 = factory.load("full")

        package_1.oversize.select("double")
        package_2.oversize.select("double")

        self.assertTrue(package_1 == package_2)
        self.assertFalse(package_1 != package_2)

    def test_should_show_different_normal_package_types_as_inequal(self):
        package_1 = factory.load("full")
        package_2 = factory.load("half")

        self.assertTrue(package_1 != package_2)
        self.assertFalse(package_1 == package_2)

    def test_should_show_different_oversize_package_types_as_inequal(self):
        package_1 = factory.load("full")

        self.assertFalse(package_1 == self._double_half)


if __name__ == '__main__':
    unittest.main()
