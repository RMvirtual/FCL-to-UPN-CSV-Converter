import unittest
from src.main.upn.api.consignment import ConsignmentApiCall


class TestUpnAPI(unittest.TestCase):
    """Muting test temporarily while work ensues elsewhere."""

    def test_should_get_post_code_restrictions(self):
        caller = ConsignmentApiCall()
        restrictions = caller.get_post_code_restrictions("AB10")
        restrictions_dict = restrictions[0]
        self.assertEqual("AB10", restrictions_dict["Postcode"])

    def test_should_get_network_input(self):
        caller = ConsignmentApiCall()
        network_input = caller.get_network_input()

        print("Printing network input:")
        print(network_input)

        self.fail("DUMMY FAIL")


if __name__ == '__main__':
    unittest.main()
