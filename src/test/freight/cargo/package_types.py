import unittest
from src.main.file_system.runfiles import load_path
from src.main.freight.cargo.types import load_package_type


class TestPackageTypesJsonReader(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_should_get_base_type_from_full_pallet(self):
        package_type = load_package_type("full")
        self.assertEqual(package_type.base_type, "pallet")

    @property
    def _test_json_file(self) -> str:
        return load_path(
            "resources/test_inputs/base_packages.json")


if __name__ == '__main__':
    unittest.main()
