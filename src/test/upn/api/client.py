import unittest
from src.main.upn.api.client import UpnApiClient


class TestUpnApiClient(unittest.TestCase):
    def test_should_get_post_code_restrictions(self):
        client = UpnApiClient()
        restrictions = client.post_code_restrictions("AB10")
        restrictions_dict = restrictions[0]
        self.assertEqual("AB10", restrictions_dict["Postcode"])

    def test_should_get_network_input(self):
        client = UpnApiClient()
        network_input = client.network_input("2022-10-18")
        correct_no_of_consignments = 174

        self.assertEqual(correct_no_of_consignments, len(network_input))

    def test_should_get_network_deliveries(self):
        client = UpnApiClient()
        network_input = client.network_deliveries("2022-10-18")
        correct_no_of_consignments = 152

        self.assertEqual(correct_no_of_consignments, len(network_input))

    def test_should_get_network_delivery_by_con_no(self):
        client = UpnApiClient()
        consignments = client.network_delivery_by_con_no("22302")
        correct_barcode = "D001446027C"

        matching_consignments = list(filter(
            lambda consignment: consignment["ConBarcode"] == correct_barcode,
            consignments
        ))

        self.assertTrue(matching_consignments)


if __name__ == '__main__':
    unittest.main()
