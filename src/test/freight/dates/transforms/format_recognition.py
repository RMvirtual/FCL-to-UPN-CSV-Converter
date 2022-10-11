import unittest
from src.main.freight.dates.format_recognition import DateFormatRecognition


class TestDateFormatRecognition(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_should_recognise_numeric_only_format(self):
        numeric_dates = ["231022", "23102022"]

        non_numeric_dates = [
            "23/10/22", "23/10/2022", "23 September 2022", "23.10.22",
            "23.10.2022", "23 10 2022", "23 10 22"
        ]

        for date in numeric_dates:
            recognition = DateFormatRecognition(date)
            self.assertTrue(recognition.is_numeric())

        for date in non_numeric_dates:
            recognition = DateFormatRecognition(date)
            self.assertFalse(recognition.is_numeric())


if __name__ == '__main__':
    unittest.main()
