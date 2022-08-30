import unittest
from src.main.freight.service.options import ServiceOptions


class TestServiceOptions(unittest.TestCase):
    def setUp(self) -> None:
        self._service_options = ServiceOptions()

    def test_should_create_default_service_options(self):
        default_service_checks = [
            self._service_options.main_service.is_next_day(),
            self._service_options.premium_service.is_not_required(),
            self._service_options.additional_service.is_not_required(),
            self._service_options.tail_lift.is_not_required()
        ]

        for check in default_service_checks:
            self.assertTrue(check)

    def test_should_amend_service_options(self):
        self._service_options.main_service.economy()
        self._service_options.premium_service.timed()
        self._service_options.additional_service.book_in()
        self._service_options.tail_lift.required()

        amended_service_checks = [
            self._service_options.main_service.is_economy(),
            self._service_options.premium_service.is_timed(),
            self._service_options.additional_service.is_book_in(),
            self._service_options.tail_lift.is_required()
        ]

        for check in amended_service_checks:
            self.assertTrue(check)


if __name__ == '__main__':
    unittest.main()
