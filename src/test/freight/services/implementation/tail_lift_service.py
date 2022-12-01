import unittest
from src.main.freight.services.implementation.tail_lift import TailLiftService


class TestTailLiftService(unittest.TestCase):
    def setUp(self):
        self._service = TailLiftService()

    def test_should_change_service(self) -> None:
        self._service.required()
        self.assertTrue(self._service.is_required())
        self.assertFalse(self._service.is_not_required())

    def test_should_show_service_as_true_when_required(self) -> None:
        self.assertFalse(self._service)
        self._service.required()
        self.assertTrue(self._service)

    def test_should_show_two_services_as_equal(self) -> None:
        other_service = TailLiftService()
        self.assertEqual(self._service, other_service)

        other_service.required()
        self.assertNotEqual(self._service, other_service)


if __name__ == "__main__":
    unittest.main()
