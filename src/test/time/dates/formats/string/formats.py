import unittest
from src.main.time.dates.formats.string import formats


class TestDateFormatRecognition(unittest.TestCase):
    def test_should_format_dd_mm_yy(self) -> None:
        result = formats.DDMMYY("030691")

        self.assertEqual(3, result.day)
        self.assertEqual(6, result.month)
        self.assertEqual(91, result.year)

    def test_should_format_dd_mm_yyyy(self) -> None:
        result = formats.DDMMYYYY("03061991")

        self.assertEqual(3, result.day)
        self.assertEqual(6, result.month)
        self.assertEqual(1991, result.year)

    def test_should_format_dd_mm_yy_with_separators(self) -> None:
        for date in ["03/06/91", "03.06.91"]:
            result = formats.NumericWithSeparators(date)
            self.assertEqual(3, result.day)
            self.assertEqual(6, result.month)
            self.assertEqual(91, result.year)

    def test_should_format_dd_mm_yyyy_with_separators(self) -> None:
        for date in ["03/06/1991", "03.06.1991"]:
            result = formats.NumericWithSeparators(date)
            self.assertEqual(3, result.day)
            self.assertEqual(6, result.month)
            self.assertEqual(1991, result.year)

    def test_should_format_dd_mm_yyyy_with_whitespace(self) -> None:
        result = formats.NumericWithSeparators("03 06 91")

        self.assertEqual(3, result.day)
        self.assertEqual(6, result.month)
        self.assertEqual(91, result.year)


if __name__ == '__main__':
    unittest.main()
