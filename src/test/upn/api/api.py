import unittest
from src.main.upn.api.consignment import ConsignmentApiCall


@unittest.SkipTest
class TestUpnAPI(unittest.TestCase):
    """Muting test temporarily while work ensues elsewhere."""
    def test_should_get_network_deliveries(self):
        caller = ConsignmentApiCall()
        caller.get_network_input()

        self.fail("DUMMY FAIL")


if __name__ == '__main__':
    unittest.main()
