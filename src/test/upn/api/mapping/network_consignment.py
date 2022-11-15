import unittest

from src.main.upn.api.mapping.network_consignment \
    import NetworkConsignmentConversion

from src.test.upn.api.mapping.setup import upn_setup, freight_setup


class TestNetworkConsignmentMapping(unittest.TestCase):
    def setUp(self):
        self._network_consignment = upn_setup.dummy_network_consignment()
        self._correct_freight_consignment = freight_setup.dummy_consignment()

    def test_should_map_network_consignment_to_house_consignment(self):
        self.fail("DUMMY FAIL")


if __name__ == '__main__':
    unittest.main()
