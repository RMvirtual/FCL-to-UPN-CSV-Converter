import unittest
from src.main.freight.service.validation import ServiceValidationStrategy
from src.main.freight.service.types import (
    MainService, PremiumService, BookedService)


class TestServiceValidation(unittest.TestCase):
    def test_should_validate_adding_a_booked_service(self):
        priority = MainService.PRIORITY
        premium = None
        booked = None

        validator = ServiceValidationStrategy(priority, premium, booked)
        self.assertFalse(validator.can_have_booked_service())

        priority = MainService.ECONOMY
        self.assertTrue(validator.can_have_booked_service())


if __name__ == '__main__':
    unittest.main()
