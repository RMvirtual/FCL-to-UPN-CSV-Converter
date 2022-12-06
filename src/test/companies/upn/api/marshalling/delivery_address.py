import unittest
from src.main.companies.upn.api.marshalling import delivery_address


class TestUPNDeliveryAddressUnmarshaller(unittest.TestCase):
    def setUp(self):
        self._raw_input = {
            'DeliveryCoName': 'GRAYLAW FREIGHT GROUP',
            'DeliveryAdd1': 'GRAYLAW FREIGHT TERMINAL',
            'DeliveryAdd2': 'GILLBRANDS ROAD',
            'DeliveryTown': 'SKELMERSDALE',
            'DeliveryCounty': 'LANCS',
            'DeliveryPostcode': 'WN8 9TA',
            'DeliveryCountry': 'UNITED KINGDOM',
            'DeliveryContactName': 'Katherine   01695 729101',
            'DeliveryPhone': '0',
        }

    def test_should_unmarshall_basic_next_day_services(self) -> None:
        result = delivery_address.unmarshall(self._raw_input)
        self.assertEqual("GRAYLAW FREIGHT GROUP", result.name)
        self.assertEqual("GRAYLAW FREIGHT TERMINAL", result.line_1)
        self.assertEqual("GILLBRANDS ROAD", result.line_2)
        self.assertEqual("SKELMERSDALE", result.town)
        self.assertEqual("LANCS", result.county)
        self.assertEqual("WN8 9TA", result.post_code)
        self.assertEqual("UNITED KINGDOM", result.country)
        self.assertEqual("Katherine   01695 729101", result.contact_name)
        self.assertEqual("0", result.telephone_no)


if __name__ == "__main__":
    unittest.main()
