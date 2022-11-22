import datetime
import unittest
from src.main.upn.consignment.adaptors.date import UPNDateAdaptor


class TestDateAdaptor(unittest.TestCase):
    def setUp(self):
        self._date = datetime.datetime(day=3, month=6, year=1991)
        self._adaptor = UPNDateAdaptor(self._date)

    def test_should_get_day(self) -> None:
        self.assertEqual(3, self._adaptor.day)

    def test_should_get_month(self) -> None:
        self.assertEqual(6, self._adaptor.month)

    def test_should_get_year(self) -> None:
        self.assertEqual(1991, self._adaptor.year)


if __name__ == '__main__':
    unittest.main()
