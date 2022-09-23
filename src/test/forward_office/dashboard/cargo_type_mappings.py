import unittest
from src.main.forward_office.dashboard.cargo_type_mappings \
    import FclCargoTypeMappings


class TestFclCargoTypeMappings(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_should_map_fcl_cargo_type(self):
        cargo_types = FclCargoTypeMappings()
        package_type = cargo_types.PALL

        self.assertEqual("full", package_type.name)
        self.assertEqual("pallet", package_type.base_type)


if __name__ == '__main__':
    unittest.main()
