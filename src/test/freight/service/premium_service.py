import unittest
from src.main.freight.service.premium.implementation import PremiumService


class TestPremiumService(unittest.TestCase):
    def setUp(self):
        self._service = PremiumService()

    def test_should_set_service_as_am(self) -> None:
        self._service.am()
        self.assertTrue(self._service.is_am())
        self.assertFalse(self._service.is_timed())

    def test_should_show_service_as_true_when_not_none(self) -> None:
        self.assertFalse(self._service)
        self._service.pre_10am()
        self.assertTrue(self._service)


if __name__ == "__main__":
    unittest.main()
