import unittest
from src.main.freight.cargo.packages.oversize import factory
from src.main.freight.cargo.packages.oversize.options import (
    OversizeOption, OversizeOptions)


class TestLoadingOversizeOptionsFromFile(unittest.TestCase):
    def test_should_get_options_by_base_type(self):
        options = factory.options_by_base_type("pallet")
        correct = self._correct_options()
        self.assertEqual(correct.selected, options.selected)
        self.assertEqual(correct.default, options.default)
        self.assertListEqual(correct.values, options.values)

    def test_should_get_all_options(self):
        all_options = factory.all_options()
        pallet_options = all_options["pallet"]
        correct = self._correct_options()

        self.assertTrue("pallet" in all_options)
        self.assertEqual(correct.selected, pallet_options.selected)
        self.assertEqual(correct.default, pallet_options.default)
        self.assertListEqual(correct.values, pallet_options.values)

    def _correct_options(self):
        options = self._correct_values()

        return OversizeOptions(default=options[0], options=options)

    @staticmethod
    def _correct_values() -> list[OversizeOption]:
        options = {"normal": 1, "oversize": 1.5, "double": 2, "triple": 3}

        return [
            OversizeOption(name, multiplier)
            for name, multiplier in list(options.items())
        ]


if __name__ == '__main__':
    unittest.main()
