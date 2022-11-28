import unittest
from src.main.upn.freight.address.address import UPNAddress
from src.main.third_party_bridges.graylaw_upn.adaptors.address import UPNAddressAdaptor


class TestUPNAddressAdaptor(unittest.TestCase):
    def setUp(self):
        self._address = UPNAddress()
        self._address.name = "Graylaw International"
        self._address.line_1 = "Gillibrands Road"
        self._address.line_2 = "West Pimbo"
        self._address.town = "Skelmersdale"
        self._address.county = "Lancashire"
        self._address.post_code = "WN8 9TA"
        self._address.country = "GB"
        self._address.contact_name = "Ryan Matfen"
        self._address.telephone_no = "01695 729101"

    def test_should_adapt_upn_address(self) -> None:
        adapted_address = UPNAddressAdaptor(self._address)
        self.assertEqual("Graylaw International", adapted_address.name)

        self.assertListEqual(
            ["Gillibrands Road", "West Pimbo", "Lancashire"],
            adapted_address.lines
        )

        self.assertEqual("Skelmersdale", adapted_address.town)
        self.assertEqual("WN8 9TA", adapted_address.post_code)
        self.assertEqual("GB", adapted_address.country)
        self.assertEqual("Ryan Matfen", adapted_address.contact_name)
        self.assertEqual("01695 729101", adapted_address.telephone_number)


if __name__ == '__main__':
    unittest.main()
