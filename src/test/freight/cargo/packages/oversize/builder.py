import unittest
from src.main.freight.cargo.packages.oversize.builder \
    import OversizeOptionsBuilder


class TestOversizeOptionsBuilder(unittest.TestCase):
    def setUp(self):
        pass

    def test_should_build_one_option(self) -> None:
        builder = OversizeOptionsBuilder()
        correct_name = "normal"
        correct_multiplier = 1
        builder.add_option(correct_name, correct_multiplier)

        result = builder.build()
        self.assertEqual(1, len(result))

        option = result[correct_name]
        self.assertEqual(correct_name, option.name)
        self.assertEqual(correct_multiplier, option.multiplier)


if __name__ == '__main__':
    unittest.main()
