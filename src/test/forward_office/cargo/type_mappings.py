import unittest
from src.main.forward_office.cargo.type_mappings \
    import FclCargoTypeMap


class TestFclCargoTypeMappings(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_should_map_fcl_cargo_type(self):
        cargo_types = FclCargoTypeMap()
        package_type = cargo_types.PAL2

        self.assertEqual("full", package_type.name)
        self.assertEqual("pallet", package_type.base_type)
        self.assertEqual("double", package_type.oversize_option)


if __name__ == '__main__':
    unittest.main()
