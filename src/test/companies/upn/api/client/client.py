import unittest
from src.main.companies.upn.api.client.soap_api import UPNAPIClient


class TestUpnApiClient(unittest.TestCase):
    def setUp(self):
        self._client = UPNAPIClient()

    def test_should_get_post_code_restrictions(self):
        post_code = "AB10"

        matching_restrictions = list(filter(
            lambda restriction: restriction["Postcode"] == post_code,
            self._client.post_code_restrictions(post_code)
        ))

        self.assertTrue(matching_restrictions)

    def test_should_get_network_input(self):
        network_input = self._client.network_input("2022-10-18")
        correct_no_of_consignments = 174

        self.assertEqual(correct_no_of_consignments, len(network_input))

    def test_should_get_network_deliveries(self):
        network_input = self._client.network_deliveries("2022-10-18")
        correct_no_of_consignments = 152

        self.assertEqual(correct_no_of_consignments, len(network_input))

    def test_should_get_network_delivery_by_con_no(self):
        consignments = self._client.network_delivery_by_con_no("22302")
        correct_barcode = "D001446027C"

        matching_consignments = list(filter(
            lambda consignment: consignment["ConBarcode"] == correct_barcode,
            consignments
        ))

        self.assertTrue(matching_consignments)


if __name__ == '__main__':
    unittest.main()
