import unittest
from src.main.freight.shipment_dates.implementation import ShipmentDates


class TestShipmentDates(unittest.TestCase):
    def setUp(self) -> None:
        self._dates = ShipmentDates()

    def test_collection_cannot_be_later_than_delivery(self) -> None:
        with self.assertRaises(ValueError):
            self._dates.delivery_date = "03/06/1991"
            self._dates.collection_date = "04/06/1991"


if __name__ == '__main__':
    unittest.main()
