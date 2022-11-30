import unittest
from src.main.time.dates.formats.implementation import NumericFormatter


class TestNumericDateFormatter(unittest.TestCase):
    def test_should_format_dd_mm_yy(self) -> None:
        result = NumericFormatter("030691")

        self.assertEqual(3, result.day)
        self.assertEqual(6, result.month)
        self.assertEqual(2091, result.year)

    def test_should_format_dd_mm_yyyy(self) -> None:
        result = NumericFormatter("03061991")

        self.assertEqual(3, result.day)
        self.assertEqual(6, result.month)
        self.assertEqual(1991, result.year)


if __name__ == '__main__':
    unittest.main()
