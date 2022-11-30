import unittest
from src.main.time.dates.formats import factory
from src.main.time.dates.formats.interface import DateFormatter


class TestDateFormatterFactory(unittest.TestCase):
    def setUp(self) -> None:
        self._numeric_dates = ["030691", "03061991"]

        self._numeric_delimited_dates = [
            "3/6/91", "3/06/91", "03/06/91", "03/06/1991",
            "3.6.91", "3.06.91", "03.06.91", "03.06.1991",
            "3 6 91", "3 06 91", "03 06 91", "03 06 1991",
        ]

        self._alphanumeric_dates = [
            "03 June 1991", "03 Jun 91", "03/June/1991", "3/June/91"
            "3.June.91", "3.Jun.91"
        ]

        self._unrecognisable_dates = [
            "24th January 2019", "Last Week", "11122"]

    def test_should_format_numeric_dates(self) -> None:
        for date in self._numeric_dates:
            self._assert_matches_03_06_1991(factory.formatter(date))

    def test_should_format_numeric_delimited_dates(self) -> None:
        for date in self._numeric_delimited_dates:
            self._assert_matches_03_06_1991(factory.formatter(date))

    def test_should_format_alphanumeric_dates(self) -> None:
        for date in self._numeric_delimited_dates:
            self._assert_matches_03_06_1991(factory.formatter(date))

    def test_should_raise_exception_when_formatting_invalid_date(self) -> None:
        for date in self._unrecognisable_dates:
            self._assert_date_formatting_raises_exception(date)

    def _assert_date_formatting_raises_exception(self, date: str) -> None:
        with self.assertRaises(ValueError):
            _ = factory.formatter(date)

    def _assert_matches_03_06_1991(self, formatter: DateFormatter) -> None:
        self.assertEqual(3, formatter.day)
        self.assertEqual(6, formatter.month)
        self.assertEqual(1991, formatter.year)


if __name__ == '__main__':
    unittest.main()
