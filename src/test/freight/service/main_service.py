import unittest
from src.main.freight.service.main.implementation import MainService


class TestMainService(unittest.TestCase):
    def setUp(self):
        self._service = MainService()

    def test_should_set_service_as_next_day(self) -> None:
        self._service.next_day()

        self.assertTrue(self._service.is_next_day())
        self.assertFalse(self._service.is_economy())

    def test_should_set_service_as_economy(self) -> None:
        self._service.economy()

        self.assertTrue(self._service.is_economy())
        self.assertFalse(self._service.is_next_day())


if __name__ == "__main__":
    unittest.main()
