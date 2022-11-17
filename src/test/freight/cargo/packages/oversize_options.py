import unittest
from src.main.freight.cargo.packages.oversize import factory
from src.main.freight.cargo.packages.oversize.options import OversizeOption


class TestLoadingOversizeOptionsFromFile(unittest.TestCase):
    def test_should_get_options_by_base_type(self):
        self.assertListEqual(
            self._correct_options(), factory.options_by_base_type("pallet"))

    def test_should_get_all_options(self):
        self.assertDictEqual(
            self._correct_packages_to_options(), factory.all_options())

    def _correct_packages_to_options(self):
        return {"pallet": self._correct_options()}

    @staticmethod
    def _correct_options():
        options = {"normal": 1, "oversize": 1.5, "double": 2, "triple": 3}

        return [
            OversizeOption(name, multiplier)
            for name, multiplier in list(options.items())
        ]


if __name__ == '__main__':
    unittest.main()
