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

    def test_should_recognise_numeric_formats(self):
        for date in self._numeric_dates:
            self.assertTrue(DateFormat(date).is_numeric())

        for date in self._numeric_delimited_dates + self._alphanumeric_dates:
            self.assertFalse(DateFormat(date).is_numeric())

    def test_should_recognise_numeric_delimited_formats(self):
        for date in self._numeric_delimited_dates:
            self.assertTrue(DateFormat(date).is_numeric_with_delimiters())

        for date in self._numeric_dates + self._alphanumeric_dates:
            self.assertFalse(DateFormat(date).is_numeric_with_delimiters())

    def test_should_recognise_alphabetic_format(self):
        for date in self._alphanumeric_dates:
            self.assertTrue(DateFormat(date).is_alphanumeric())

        for date in self._numeric_dates + self._numeric_delimited_dates:
            self.assertFalse(DateFormat(date).is_alphanumeric())


if __name__ == '__main__':
    unittest.main()
