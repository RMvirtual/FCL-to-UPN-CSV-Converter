import unittest
from src.test.graylaw.cargo.packages.types.builder import setup
from src.main.graylaw.cargo.packages.types.builder import PackageTypeBuilder


class TestPackageTypeBuilder(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_should_build_normal_full_pallet(self) -> None:
        builder = PackageTypeBuilder()
        builder.set_base_type("pallet")
        builder.set_name("full")
        builder.set_max_weight(1200)

        max_dimensions = setup.dimensions()
        builder.set_max_dimensions(max_dimensions)

        oversize_options = setup.oversize_options()
        builder.set_oversize_options(oversize_options)

        result = builder.build()
        correct_dimensions = setup.dimensions()

        self.assertEqual("pallet", result.base_type)
        self.assertEqual("full", result.name)
        self.assertEqual(1200, result.maximum_weight)
        self.assertEqual(correct_dimensions, result.maximum_dimensions)
        self.assertEqual(oversize_options, result.oversize)


if __name__ == '__main__':
    unittest.main()
