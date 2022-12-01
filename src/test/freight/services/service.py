import unittest
from src.main.freight.services.validation import ServiceValidationStrategy
from src.main.freight.services.types import ServiceOptions, MainService


class TestServiceValidation(unittest.TestCase):
    def test_should_validate_adding_a_booked_service(self):
        service_options = ServiceOptions()
        validator = ServiceValidationStrategy(service_options)
        self.assertFalse(validator.can_have_booked_service())

        service_options.main_service = MainService.ECONOMY
        self.assertTrue(validator.can_have_booked_service())


if __name__ == '__main__':
    unittest.main()
