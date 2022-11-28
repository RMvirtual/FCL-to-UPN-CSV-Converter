import unittest
from src.main.third_party_bridges.graylaw_forward_office.mapping.cargo import FclCargoTypeMap


class TestFCLCargoTypeMappings(unittest.TestCase):
    def setUp(self) -> None:
        self._cargo_type_map = FclCargoTypeMap()

    def test_should_map_fcl_cargo_type(self):
        package_type = self._cargo_type_map.PAL2

        self.assertEqual("full", package_type.name)
        self.assertEqual("pallet", package_type.base_type)
        self.assertEqual("double", package_type.oversize.selected.name)

    def test_should_verify_if_package_type_contained(self):
        self.assertTrue(self._cargo_type_map.contains("PALL"))
        self.assertFalse(self._cargo_type_map.contains("LIFT"))


if __name__ == '__main__':
    unittest.main()
