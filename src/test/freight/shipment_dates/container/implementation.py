import unittest
from src.main.freight.shipment_dates.container.implementation import Date


class TestShipmentDates(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_collection_cannot_be_earlier_than_delivery(self) -> None:
        self.fail("MOCK FAIL")


if __name__ == '__main__':
    unittest.main()
