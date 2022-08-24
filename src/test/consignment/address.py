import unittest
from src.main.consignment.address import Address


class TestAddress(unittest.TestCase):
    def test_should_complete_address(self):
        address = Address()
        address.name = "Graylaw Freight Group"
        address.line_1 = "Gillibrands Road"
        address.town = "Skelmersdale"
        address.post_code = "WN8 9TA"
        address.country = "GB"

        self.assertTrue(address.is_valid())


if __name__ == '__main__':
    unittest.main()
