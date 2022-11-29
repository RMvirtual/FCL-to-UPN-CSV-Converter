import unittest
from src.main.freight.shipment_dates.date.factory.integers \
    import DateAsIntegersFactory


class TestDatesAsIntegersFactory(unittest.TestCase):
    def setUp(self):
        self._factory = DateAsIntegersFactory()

    def test_should_create_from_dd_mm_yyyy(self):
        date = self._factory.from_dd_mm_yy("03061991")

        self.assertEqual(3, date.day)
        self.assertEqual(6, date.month)
        self.assertEqual(1991, date.year)


if __name__ == '__main__':
    unittest.main()
