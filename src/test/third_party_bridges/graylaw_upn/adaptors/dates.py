import datetime
import unittest
from src.main.upn.freight.dates.dates import UPNDates
from src.main.third_party_bridges.graylaw_upn.adaptors.dates import UPNDatesAdaptor


class TestUPNDatesAdaptor(unittest.TestCase):
    def setUp(self):
        dates_to_adapt = UPNDates()
        dates_to_adapt.delivery = datetime.datetime(
            day=3, month=6, year=1991, hour=13, minute=30)

        dates_to_adapt.despatch = datetime.datetime(day=2, month=6, year=1991)
        self._adaptor = UPNDatesAdaptor(dates_to_adapt)

    def test_should_get_delivery_date(self) -> None:
        date = self._adaptor.delivery_date
        self.assertEqual(3, date.day)
        self.assertEqual(6, date.month)
        self.assertEqual(1991, date.year)

    def test_should_get_delivery_time(self) -> None:
        time = self._adaptor.delivery_time
        self.assertEqual(13, time.hour)
        self.assertEqual(30, time.minute)

    def test_should_get_collection_date(self) -> None:
        date = self._adaptor.collection_date
        self.assertEqual(2, date.day)
        self.assertEqual(6, date.month)
        self.assertEqual(1991, date.year)


if __name__ == '__main__':
    unittest.main()
