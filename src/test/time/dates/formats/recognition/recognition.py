import unittest
from src.main.time.dates.formats.recognition import DateFormat


class TestDateFormatRecognition(unittest.TestCase):
    def setUp(self) -> None:
        self._numeric_dates = ["231022", "23102022"]

        self._numeric_delimited_dates = [
            "23/10/22", "23/10/2022", "23.10.22", "23.10.2022",
            "23 10 2022", "23 10 22"
        ]

        self._alphanumeric_dates = [
            "23 September 2022", "03 Jun 22", "03/June/1991"]

    def test_should_recognise_numeric_formats(self) -> None:
        for date in self._numeric_dates:
            self.assertTrue(DateFormat(date).is_numeric())

        for date in self._numeric_delimited_dates + self._alphanumeric_dates:
            self.assertFalse(DateFormat(date).is_numeric())

    def test_should_recognise_numeric_delimited_formats(self) -> None:
        for date in self._numeric_delimited_dates:
            self.assertTrue(DateFormat(date).is_numeric_with_delimiters())

        for date in self._numeric_dates + self._alphanumeric_dates:
            self.assertFalse(DateFormat(date).is_numeric_with_delimiters())

    def test_should_recognise_alphabetic_format(self) -> None:
        for date in self._alphanumeric_dates:
            self.assertTrue(DateFormat(date).is_alphanumeric())

        for date in self._numeric_dates + self._numeric_delimited_dates:
            self.assertFalse(DateFormat(date).is_alphanumeric())

    def test_should_not_recognise_format(self) -> None:
        unrecognisable_dates = ["24th January 2019", "Last Week", "11122"]

        recognisable_dates = (
            self._numeric_dates
            + self._numeric_delimited_dates
            + self._alphanumeric_dates
        )

        for date in unrecognisable_dates:
            self.assertTrue(DateFormat(date).is_unrecognised())

        for date in recognisable_dates:
            self.assertFalse(DateFormat(date).is_unrecognised())


if __name__ == '__main__':
    unittest.main()
