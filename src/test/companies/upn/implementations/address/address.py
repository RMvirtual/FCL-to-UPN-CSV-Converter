import unittest
from src.main.companies.upn.implementations.address.address import UPNAddress


class TestUPNAddress(unittest.TestCase):
    def setUp(self):
        self._address = UPNAddress()

    def test_should_set_address_lines(self) -> None:
        self._set_up_graylaw_lines()
        self.assertEqual("Gillibrands Road", self._address.line_1)
        self.assertEqual("West Pimbo", self._address.line_2)
        self.assertEqual("Lancashire", self._address.county)

    def test_should_modify_line(self) -> None:
        self._set_up_graylaw_lines()
        self._address.line_2 = "East Pimbo"
        self.assertEqual("East Pimbo", self._address.line_2)

    def test_should_get_empty_string_when_no_line(self) -> None:
        self.assertEqual("", self._address.line_1)
        self.assertEqual("", self._address.line_2)
        self.assertEqual("", self._address.county)

    def test_should_push_line_mutators_to_prior_empty_lines(self):
        self._address.county = "Lancashire"
        self.assertEqual("Lancashire", self._address.line_1)
        self.assertEqual("", self._address.line_2)

    def _set_up_graylaw_lines(self) -> None:
        self._address.line_1 = "Gillibrands Road"
        self._address.line_2 = "West Pimbo"
        self._address.county = "Lancashire"


if __name__ == '__main__':
    unittest.main()
