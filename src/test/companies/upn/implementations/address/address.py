import unittest
from src.main.companies.upn.implementations.address.address import UPNAddress


class TestUPNAddress(unittest.TestCase):
    def setUp(self):
        self._address = UPNAddress()
        self._address.line_1 = "Gillibrands Road"
        self._address.line_2 = "West Pimbo"
        self._address.county = "Lancashire"

    def test_should_set_address_lines(self) -> None:
        self.assertEqual("Gillibrands Road", self._address.line_1)
        self.assertEqual("West Pimbo", self._address.line_2)
        self.assertEqual("Lancashire", self._address.county)

    def test_should_modify_line(self) -> None:
        self._address.line_2 = "East Pimbo"
        self.assertEqual("East Pimbo", self._address.line_2)


if __name__ == '__main__':
    unittest.main()
