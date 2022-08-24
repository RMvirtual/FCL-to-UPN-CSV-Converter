import unittest
from src.main.consignment.address import Address


class TestAddress(unittest.TestCase):
    def setUp(self) -> None:
        self._address = Address()
        self._address.name = "Graylaw Freight Group"
        self._address.line_1 = "Gillibrands Road"
        self._address.town = "Skelmersdale"
        self._address.post_code = "WN8 9TA"
        self._address.country = "GB"

    def test_should_validate_sufficient_address(self):
        self.assertTrue(self._address.is_valid())

    def test_should_invalidate_incorrect_post_code(self):
        incorrect_post_code = "1L43 8EP"

        with self.assertRaises(ValueError):
            self._address.post_code = incorrect_post_code


if __name__ == '__main__':
    unittest.main()
