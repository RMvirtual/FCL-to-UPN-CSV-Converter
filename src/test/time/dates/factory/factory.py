import unittest
from src.main.time.dates.factory import dates as date_factory
from src.main.time.dates.interface.date import DateInterface


class TestDateFactory(unittest.TestCase):
    def setUp(self) -> None:
        self._correct_day = 23
        self._correct_month = 10
        self._correct_year = 2022

    def test_should_create_from_numeric_date(self) -> None:
        self._assert_list_produces_03_06_2022(["030622", "03062022"])

    def test_should_create_from_numeric_delimited_date(self) -> None:
        dates = [
            "03\\06\\2022", "03-06-2022", "03/06/2022", "03.06.2022",
            "03\\06\\22", "03-06-22", "03/06/22", "03.06.22",
            "3.6.22", "03.6.22", "3.06.22"
        ]

        self._assert_list_produces_03_06_2022(dates)

    def test_should_create_from_alphanumeric_date(self) -> None:
        dates = [
            "03-Jun-2022", "03-Jun-22", "03-June-2022", "03-June-22",
            "03/June/22", "03 June 2022", "3 June 22", " 03 June 2022"
        ]

        self._assert_list_produces_03_06_2022(dates)

    def _assert_list_produces_03_06_2022(self, dates: list[str]) -> None:
        for date in dates:
            self._assert_date_is_03_06_2022(date_factory.from_string(date))

    def _assert_date_is_03_06_2022(self, date: DateInterface) -> None:
        self.assertEqual(3, date.day)
        self.assertEqual(6, date.month)
        self.assertEqual(2022, date.year)


if __name__ == '__main__':
    unittest.main()
