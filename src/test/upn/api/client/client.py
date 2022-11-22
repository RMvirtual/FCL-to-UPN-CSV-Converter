import unittest
from src.main.upn.api.client.soap_api import UPNAPIClient


class TestUpnApiClient(unittest.TestCase):
    def test_should_get_post_code_restrictions(self):
        client = UPNAPIClient()
        post_code = "AB10"

        matching_retrictions = list(filter(
            lambda restriction: restriction["Postcode"] == post_code,
            client.post_code_restrictions(post_code)
        ))

        self.assertTrue(matching_retrictions)

    def test_should_get_network_input(self):
        client = UPNAPIClient()
        network_input = client.network_input("2022-10-18")
        correct_no_of_consignments = 174

        self.assertEqual(correct_no_of_consignments, len(network_input))

    def test_should_get_network_deliveries(self):
        client = UPNAPIClient()
        network_input = client.network_deliveries("2022-10-18")
        correct_no_of_consignments = 152

        self.assertEqual(correct_no_of_consignments, len(network_input))

    def test_should_get_network_delivery_by_con_no(self):
        client = UPNAPIClient()
        consignments = client.network_delivery_by_con_no("22302")
        correct_barcode = "D001446027C"

        matching_consignments = list(filter(
            lambda consignment: consignment["ConBarcode"] == correct_barcode,
            consignments
        ))

        self.assertTrue(matching_consignments)


if __name__ == '__main__':
    unittest.main()
