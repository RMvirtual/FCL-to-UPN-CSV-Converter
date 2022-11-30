import unittest
from src.main.time.dates.formats.recognition import DateFormat


class TestDateFormatRecognition(unittest.TestCase):
    def setUp(self) -> None:
        self._numeric_dates = ["231022", "23102022", "03061991"]

        self._numeric_delimited_dates = [
            "23/10/22", "23/10/2022", "23.10.22", "23.10.2022",
            "23 10 2022", "23 10 22", "3/6/91", "3/06/91",
            "03/06/91"
        ]

        self._alphanumeric_dates = [
            "23 September 2022", "03 Jun 22", "03/June/1991"]

        self._unrecognisable_dates = [
            "24th January 2019", "Last Week", "11122"]

    def test_should_recognise_numeric_formats(self) -> None:
        for date in self._numeric_dates:
            self.assertTrue(DateFormat(date).is_numeric())

        non_numerics = (
            self._numeric_delimited_dates + self._alphanumeric_dates
            + self._unrecognisable_dates
        )

        for date in non_numerics:
            self.assertFalse(DateFormat(date).is_numeric())

    def test_should_recognise_numeric_delimited_formats(self) -> None:
        for date in self._numeric_delimited_dates:
            self.assertTrue(DateFormat(date).is_numeric_delimited())

        non_numeric_delimited = (
            self._numeric_dates + self._alphanumeric_dates
            + self._unrecognisable_dates
        )

        for date in non_numeric_delimited:
            self.assertFalse(DateFormat(date).is_numeric_delimited())

    def test_should_recognise_alphabetic_format(self) -> None:
        for date in self._alphanumeric_dates:
            self.assertTrue(DateFormat(date).is_alphanumeric())

        non_alphanumerics = (
            self._numeric_dates + self._numeric_delimited_dates
            + self._unrecognisable_dates
        )

        for date in non_alphanumerics:
            self.assertFalse(DateFormat(date).is_alphanumeric())

    def test_should_not_recognise_format(self) -> None:
        for date in self._unrecognisable_dates:
            self.assertTrue(DateFormat(date).is_unrecognised())

        recognisable_dates = (
            self._numeric_dates + self._numeric_delimited_dates
            + self._alphanumeric_dates
        )

        for date in recognisable_dates:
            self.assertFalse(DateFormat(date).is_unrecognised())


if __name__ == '__main__':
    unittest.main()
