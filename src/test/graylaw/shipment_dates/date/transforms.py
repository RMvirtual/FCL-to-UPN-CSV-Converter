import unittest
from src.main.graylaw.shipment_dates.date import transforms
from src.main.graylaw.shipment_dates.date.transforms import DatesAsIntegers


class TestDateTransforms(unittest.TestCase):
    def setUp(self) -> None:
        self._correct_date = DatesAsIntegers()

    def _set_up_correct_date(self, day: int, month: int, year: int) -> None:
        self._correct_date.day = day
        self._correct_date.month = month
        self._correct_date.year = year

    def test_should_transform_ddmmyyyy_without_separators(self):
        self._set_up_correct_date(23, 10, 2022)
        self._assert_date_transform_matches_correct_date("23102022")

    def test_should_transform_ddmmyyyy_with_separators(self):
        self._set_up_correct_date(23, 10, 2022)

        self._assert_date_transforms_match_correct_date(
            ["23\\10\\2022", "23-10-2022", "23/10/2022", "23.10.2022"])

    def test_should_transform_ddmmyy_without_separators(self):
        self._set_up_correct_date(23, 10, 2022)
        self._assert_date_transform_matches_correct_date("231022")

    def test_should_transform_ddmmyy_with_separators(self):
        self._set_up_correct_date(23, 10, 2022)

        self._assert_date_transforms_match_correct_date(
            ["23\\10\\22", "23-10-22", "23/10/22", "23.10.22"])

    def test_should_transform_dd_mmm_yyyy_(self):
        self._set_up_correct_date(23, 10, 2022)

        self._assert_date_transforms_match_correct_date(
            ["23-Oct-2022", "23-Oct-22"])

    def test_should_transform_dd_mmmmm_yyyy_(self):
        self._set_up_correct_date(23, 4, 2022)

        self._assert_date_transforms_match_correct_date(
            ["23-April-2022", "23-April-22"])

    def test_should_transform_date_with_full_month_name(self):
        self._set_up_correct_date(23, 9, 2022)

        self._assert_date_transforms_match_correct_date(
            ["23-September-2022", "23/September/22", " 23 September 2022"])

    def _assert_date_transforms_match_correct_date(
            self, dates: list[str]) -> None:
        for date in dates:
            self._assert_date_transform_matches_correct_date(date)

    def _assert_date_transform_matches_correct_date(self, date: str) -> None:
        dates = transforms.parse(date)
        message = "Failed date: " + date

        self.assertEqual(self._correct_date.day, dates.day, msg=message)
        self.assertEqual(self._correct_date.month, dates.month, msg=message)
        self.assertEqual(self._correct_date.year, dates.year, msg=message)


if __name__ == '__main__':
    unittest.main()
