import unittest
from src.main.addresses.validation import AddressValidationStrategy


class TestAddressValidation(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_should_invalidate_incorrect_post_code(self):
        validation = AddressValidationStrategy()
        incorrect_post_code = "1L43 8EP"

        self.assertFalse(validation.validate_post_code(incorrect_post_code))


if __name__ == '__main__':
    unittest.main()
