import unittest
from src.main.freight.cargo.oversize_options import load_oversize_option


class TestOversizeOptions(unittest.TestCase):
    def test_should_get_normal_oversize_option(self):
        package_type = load_oversize_option("normal")

        self.assertEqual("normal", package_type.name)
        self.assertDictEqual({"pallet": 1.0}, package_type.package_multipliers)


if __name__ == '__main__':
    unittest.main()
