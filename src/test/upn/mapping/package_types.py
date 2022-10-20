import unittest
from src.main.freight.cargo.package_types import load
from src.main.upn.mapping.package_types import map_to_upn_package


class TestUpnPackageTypeMappings(unittest.TestCase):
    def test_should_map_simple_pallet_type_to_upn_output(self):
        full_pallet = load("full")
        upn_package = map_to_upn_package(full_pallet)

        self.assertEqual(1, upn_package.type)
        self.assertEqual(1, upn_package.size)


if __name__ == '__main__':
    unittest.main()
