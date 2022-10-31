import unittest
from src.main.upn.api.consignment import ConsignmentApiCall


class TestUpnAPI(unittest.TestCase):
    def test_should_get_post_code_restrictions(self):
        caller = ConsignmentApiCall()
        restrictions = caller.get_post_code_restrictions("AB10")
        restrictions_dict = restrictions[0]
        self.assertEqual("AB10", restrictions_dict["Postcode"])

    def test_should_get_network_input(self):
        caller = ConsignmentApiCall()
        network_input = caller.get_network_input("2022-10-18")
        correct_no_of_consignments = 174

        self.assertEqual(correct_no_of_consignments, len(network_input))

    def test_should_get_network_deliveries(self):
        caller = ConsignmentApiCall()
        network_input = caller.get_network_deliveries("2022-10-18")
        correct_no_of_consignments = 152

        self.assertEqual(correct_no_of_consignments, len(network_input))

    def test_should_get_network_delivery_by_con_no(self):
        caller = ConsignmentApiCall()
        consignment = caller.get_network_delivery_by_con_no("GR221005418")

        print(consignment)
        self.assertEqual(1, len(consignment))
        self.fail("DUMMY FAIL")


if __name__ == '__main__':
    unittest.main()
