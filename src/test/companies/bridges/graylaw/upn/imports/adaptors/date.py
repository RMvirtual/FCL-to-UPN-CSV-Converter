import datetime
import unittest
from src.main.companies.bridges.graylaw.upn.imports.adaptors.date \
    import UPNDateAdaptor

from src.main.time.dates.factory import dates


class TestDateAdaptor(unittest.TestCase):
    def setUp(self):
        date = datetime.datetime(day=3, month=6, year=1991)
        self._adaptor = UPNDateAdaptor(date)

    def test_should_get_day(self) -> None:
        self.assertEqual(3, self._adaptor.day)

    def test_should_get_month(self) -> None:
        self.assertEqual(6, self._adaptor.month)

    def test_should_get_year(self) -> None:
        self.assertEqual(1991, self._adaptor.year)

    def test_adaptor_should_compare_as_same_date(self) -> None:
        graylaw_date = dates.from_string("03/06/1991")
        self.assertTrue(self._adaptor <= graylaw_date)
        self.assertTrue(self._adaptor == graylaw_date)
        self.assertTrue(self._adaptor >= graylaw_date)

        self.assertFalse(self._adaptor < graylaw_date)
        self.assertFalse(self._adaptor > graylaw_date)

    def test_adaptor_should_compare_as_earlier_date(self) -> None:
        graylaw_date = dates.from_string("04/06/1991")
        self.assertTrue(self._adaptor < graylaw_date)
        self.assertTrue(self._adaptor <= graylaw_date)

        self.assertFalse(self._adaptor == graylaw_date)
        self.assertFalse(self._adaptor >= graylaw_date)
        self.assertFalse(self._adaptor > graylaw_date)

    def test_adaptor_should_compare_as_later_date(self) -> None:
        graylaw_date = dates.from_string("02/06/1991")
        self.assertTrue(self._adaptor > graylaw_date)
        self.assertTrue(self._adaptor >= graylaw_date)

        self.assertFalse(self._adaptor == graylaw_date)
        self.assertFalse(self._adaptor <= graylaw_date)
        self.assertFalse(self._adaptor < graylaw_date)

    def test_adaptor_should_subtract_to_show_difference_in_days(self) -> None:
        graylaw_date = dates.from_string("08/06/1991")
        difference = self._adaptor - graylaw_date

        self.assertEqual(5, difference)


if __name__ == '__main__':
    unittest.main()
