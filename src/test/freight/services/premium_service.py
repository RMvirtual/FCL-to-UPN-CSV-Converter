import unittest
from src.main.freight.services.implementation.premium_service import PremiumService


class TestPremiumService(unittest.TestCase):
    def setUp(self):
        self._service = PremiumService()

    def test_should_change_service(self) -> None:
        self._service.am()
        self.assertTrue(self._service.is_am())
        self.assertFalse(self._service.is_timed())

    def test_should_show_service_as_true_when_not_none(self) -> None:
        self.assertFalse(self._service)
        self._service.pre_10am()
        self.assertTrue(self._service)

    def test_should_show_two_services_as_equal(self) -> None:
        other_service = PremiumService()
        self.assertEqual(self._service, other_service)

        other_service.am()
        self.assertNotEqual(self._service, other_service)


if __name__ == "__main__":
    unittest.main()
