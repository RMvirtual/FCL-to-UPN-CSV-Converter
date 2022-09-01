import unittest
from src.main.freight.cargo.oversize_options import *


class TestOversizeOptions(unittest.TestCase):
    def test_should_get_base_type_options(self):
        options = load_options_by_base_type("pallet")

        correct_options = ["normal", "oversize", "double", "triple"]
        self.assertListEqual(correct_options, list(options.keys()))


if __name__ == '__main__':
    unittest.main()
