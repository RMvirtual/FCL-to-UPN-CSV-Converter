import unittest
from src.main.upn.api.consignment import ConsignmentApiCall


class TestUpnAPI(unittest.TestCase):
    def test_should_get_network_deliveries(self):
        caller = ConsignmentApiCall()
        caller.get_network_input()

        self.fail("DUMMY FAIL")


if __name__ == '__main__':
    unittest.main()
