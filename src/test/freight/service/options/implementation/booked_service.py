import unittest
from src.main.freight.service.options.implementation.booked import BookedOption


class TestBookedService(unittest.TestCase):
    def setUp(self):
        self._service = BookedOption()

    def test_should_change_service(self) -> None:
        self._service.booked()
        self.assertTrue(self._service.is_booked())
        self.assertFalse(self._service.is_book_in())

    def test_should_show_service_as_true_when_not_none(self) -> None:
        self.assertFalse(self._service)
        self._service.booked()
        self.assertTrue(self._service)

    def test_should_show_two_services_as_equal(self) -> None:
        other_service = BookedOption()
        self.assertEqual(self._service, other_service)

        other_service.book_in()
        self.assertNotEqual(self._service, other_service)


if __name__ == "__main__":
    unittest.main()
