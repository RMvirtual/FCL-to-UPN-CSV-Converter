import unittest
from src.main.freight.cargo.packages.oversize_options import *


class TestOversizeOptions(unittest.TestCase):
    def test_should_get_options_by_base_type(self):
        options = options_by_base_type("pallet")
        correct_options = self._set_up_correct_options()

        self.assertDictEqual(correct_options, options)

    @staticmethod
    def _set_up_correct_options():
        return {
            "normal": 1,
            "oversize": 1.5,
            "double": 2,
            "triple": 3
        }

    def test_should_get_all_options(self):
        options = all_options()
        correct_options = self._set_up_all_correct_options()

        self.assertDictEqual(correct_options, options)

    @staticmethod
    def _set_up_all_correct_options():
        return {
            "pallet": {
                "normal": 1,
                "oversize": 1.5,
                "double": 2,
                "triple": 3
            }
        }


if __name__ == '__main__':
    unittest.main()
