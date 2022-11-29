import unittest
from src.main.time.dates.formats.string import formats


class TestDateFormatRecognition(unittest.TestCase):
    def setUp(self):
        ...

    def test_should_create_dd_mm_yy_format(self) -> None:
        result = formats.DDMMYY("030691")

        self.assertEqual(3, result.day)
        self.assertEqual(6, result.month)
        self.assertEqual(91, result.year)

    def test_should_create_dd_mm_yyyy_format(self) -> None:
        result = formats.DDMMYYYY("03061991")

        self.assertEqual(3, result.day)
        self.assertEqual(6, result.month)
        self.assertEqual(1991, result.year)


if __name__ == '__main__':
    unittest.main()
