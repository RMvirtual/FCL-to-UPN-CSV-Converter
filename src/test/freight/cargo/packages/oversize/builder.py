import unittest
from src.main.freight.cargo.packages.oversize.builder \
    import OversizeOptionsBuilder

from src.main.freight.cargo.packages.oversize.interface import OversizeOptions


class TestOversizeOptionsBuilder(unittest.TestCase):
    def setUp(self):
        self._builder = OversizeOptionsBuilder()

    def test_should_build_one_option(self) -> None:
        result = self._build_one_option()
        self.assertEqual(1, len(result))

        option = result["normal"]
        self.assertEqual("normal", option.name)
        self.assertEqual(1, option.multiplier)

    def test_should_build_two_options(self) -> None:
        result = self._build_two_options()
        self.assertEqual(2, len(result))

        option = result["normal"]
        self.assertEqual("normal", option.name)
        self.assertEqual(1, option.multiplier)

        option = result["double"]
        self.assertEqual("double", option.name)
        self.assertEqual(2, option.multiplier)

    def test_should_assign_default_option_at_head_of_list(self) -> None:
        self._add_double_option()
        self._builder.default_to_most_recent()
        self._add_normal_option()

        result = self._builder.build()
        self._assert_default_is_double(result)

    def test_should_assign_default_option_at_tail_of_list(self) -> None:
        self._add_both_options()
        self._builder.default_to_most_recent()

        result = self._builder.build()
        self._assert_default_is_double(result)

    def _assert_default_is_double(self, options: OversizeOptions) -> None:
        default_option = options.default

        self.assertEqual("double", default_option.name)
        self.assertEqual(2, default_option.multiplier)

    def _build_one_option(self) -> OversizeOptions:
        self._add_normal_option()

        return self._builder.build()

    def _build_two_options(self) -> OversizeOptions:
        self._add_both_options()

        return self._builder.build()

    def _add_normal_option(self) -> None:
        self._builder.add_option("normal", 1)

    def _add_double_option(self) -> None:
        self._builder.add_option("double", 2)

    def _add_both_options(self) -> None:
        self._add_normal_option()
        self._add_double_option()


if __name__ == '__main__':
    unittest.main()
