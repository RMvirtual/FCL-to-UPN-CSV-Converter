import unittest
from src.main.time.dates.formats.implementation import AlphanumericFormatter


class TestAlphanumericDateFormatter(unittest.TestCase):
    def test_should_format_full_alphanumeric_date(self) -> None:
        result = AlphanumericFormatter("03-June-1991")

        self.assertEqual(3, result.day)
        self.assertEqual(6, result.month)
        self.assertEqual(1991, result.year)

    def test_should_format_abbreviated_alphanumeric_date(self) -> None:
        result = AlphanumericFormatter("03-Jun-1991")

        self.assertEqual(3, result.day)
        self.assertEqual(6, result.month)
        self.assertEqual(1991, result.year)


if __name__ == '__main__':
    unittest.main()
