import datetime
import unittest
from src.main.upn.consignment.adaptors.date import UPNDateAdaptor
from src.main.graylaw.shipment_dates.date.model import Date as GraylawDate


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

    def test_should_show_date_as_equal(self) -> None:
        graylaw_date = GraylawDate("03/06/1991")
        self.assertEqual(graylaw_date, self._adaptor)
        self.assertFalse(graylaw_date < self._adaptor)
        self.assertFalse(graylaw_date > self._adaptor)

    def test_should_show_date_as_earlier_than(self) -> None:
        graylaw_date = GraylawDate("04/06/1991")
        self.assertLess(graylaw_date, self._adaptor)
        self.assertFalse(graylaw_date == self._adaptor)
        self.assertFalse(graylaw_date > self._adaptor)

    def test_should_show_date_as_later_than(self) -> None:
        graylaw_date = GraylawDate("02/06/1991")
        self.assertGreater(graylaw_date, self._adaptor)
        self.assertFalse(graylaw_date == self._adaptor)
        self.assertFalse(graylaw_date < self._adaptor)


if __name__ == '__main__':
    unittest.main()
