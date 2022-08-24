import unittest
from src.main.consignment.address import Address


class TestAddress(unittest.TestCase):
    def test_should_complete_address(self):
        address = Address()

        self.assertTrue(address.is_valid())


if __name__ == '__main__':
    unittest.main()
