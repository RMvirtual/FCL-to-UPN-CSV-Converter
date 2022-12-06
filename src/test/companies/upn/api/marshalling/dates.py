import datetime
import unittest
from src.main.companies.upn.api.marshalling import dates


class TestUPNServicesUnmarshaller(unittest.TestCase):
    def setUp(self):
        self._raw_input = {
            'DespatchDate': datetime.datetime(1991, 6, 3, 0, 0),
            'DeliveryDateTime': datetime.datetime(1991, 6, 4, 16, 30),
        }

    def test_should_unmarshall_dates(self) -> None:
        result = dates.unmarshall(self._raw_input)

        despatch = result.despatch_date
        self.assertEqual(3, despatch.day)
        self.assertEqual(6, despatch.month)
        self.assertEqual(1991, despatch.year)

        delivery = result.delivery_datetime
        self.assertEqual(4, delivery.day)
        self.assertEqual(6, delivery.month)
        self.assertEqual(1991, delivery.year)
        self.assertEqual(16, delivery.hour)
        self.assertEqual(30, delivery.minute)


if __name__ == "__main__":
    unittest.main()
