import unittest

from src.main.graylaw.shipment_dates.date.format_recognition \
    import DateFormatRecognition


class TestDateFormatRecognition(unittest.TestCase):
    def setUp(self) -> None:
        self._valid_dates = []
        self._invalid_dates = []

    def test_should_recognise_numeric_only_format(self):
        self._valid_dates = ["231022", "23102022"]

        self._invalid_dates = [
            "23/10/22", "23/10/2022", "23 September 2022", "23.10.22",
            "23.10.2022", "23 10 2022", "23 10 22"
        ]

        self._predicate_against_values(DateFormatRecognition.is_numeric)

    def test_should_recognise_alphabetic_format(self):
        self._valid_dates = ["23 September 2022"]

        self._invalid_dates = [
            "231022", "23102022", "23/10/22", "23/10/2022",
            "23.10.22", "23.10.2022", "23 10 2022", "23 10 22"
        ]

        self._predicate_against_values(DateFormatRecognition.is_alphanumeric)

    def test_should_recognise_separated_formats(self):
        self._valid_dates = [
            "23/10/22", "23/10/2022", "23.10.22", "23.10.2022"]

        self._invalid_dates = [
            "231022", "23102022", "23 10 2022", "23 10 22",
            "23 September 2022"
        ]

        self._predicate_against_values(DateFormatRecognition.has_separators)

    def test_should_recognise_whitespace_formats(self):
        self._valid_dates = [
            "23 10 2022", "23 10 22", "23 September 2022"]

        self._invalid_dates = [
            "23/10/22", "23/10/2022", "23.10.22", "23.10.2022",
            "231022", "23102022"
        ]

        self._predicate_against_values(DateFormatRecognition.has_whitespace)

    def _predicate_against_values(self, callback):
        self._predicate_valid_values_are_true(callback)
        self._predicate_invalid_values_are_false(callback)

    def _predicate_valid_values_are_true(self, predicate_callback) -> None:
        for date in self._valid_dates:
            self.assertTrue(
                predicate_callback(DateFormatRecognition(date)), msg=date)

    def _predicate_invalid_values_are_false(self, predicate_callback) -> None:
        for date in self._invalid_dates:
            self.assertFalse(
                predicate_callback(DateFormatRecognition(date)), msg=date)


if __name__ == '__main__':
    unittest.main()
