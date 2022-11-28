import unittest
from src.main.freight.cargo.packages.oversize.implementation import (
    OversizeOption, OversizeOptions)


class TestOversizeOptions(unittest.TestCase):
    def setUp(self):
        pass

    def test_should_show_oversize_options_as_equal(self) -> None:
        self.assertEqual(self._multiple_options(), self._multiple_options())

    def test_should_show_oversize_options_as_inequal(self) -> None:
        self.assertNotEqual(
            self._multiple_options(), self._single_option_only())

    @staticmethod
    def _multiple_options() -> OversizeOptions:
        options = [
            OversizeOption("normal", 1.0), OversizeOption("oversize", 1.5),
            OversizeOption("double", 2.0), OversizeOption("triple", 3.0)
        ]

        return OversizeOptions(default=options[0], options=options)

    @staticmethod
    def _single_option_only() -> OversizeOptions:
        only_option = OversizeOption("normal", 1.0)

        return OversizeOptions(default=only_option, options=[only_option])


if __name__ == '__main__':
    unittest.main()
