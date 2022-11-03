import unittest
from src.main.upn.api.consignment import UpnSoapApi


class TestUpnAPI(unittest.TestCase):
    def test_should_get_post_code_restrictions(self):
        caller = UpnSoapApi()
        restrictions = caller.get_post_code_restrictions("AB10")
        restrictions_dict = restrictions[0]
        self.assertEqual("AB10", restrictions_dict["Postcode"])

    def test_should_get_network_input(self):
        caller = UpnSoapApi()
        network_input = caller.get_network_input("2022-10-18")
        correct_no_of_consignments = 174

        self.assertEqual(correct_no_of_consignments, len(network_input))

    def test_should_get_network_deliveries(self):
        caller = UpnSoapApi()
        network_input = caller.get_network_deliveries("2022-10-18")
        correct_no_of_consignments = 152

        self.assertEqual(correct_no_of_consignments, len(network_input))

    def test_should_get_network_delivery_by_con_no(self):
        caller = UpnSoapApi()
        consignments = caller.get_network_delivery_by_con_no("22302")
        correct_barcode = "D001446027C"

        barcode_matches = False

        for con in consignments:
            barcode_matches = con["ConBarcode"] == correct_barcode

            if barcode_matches:
                break

        self.assertTrue(barcode_matches)


if __name__ == '__main__':
    unittest.main()
