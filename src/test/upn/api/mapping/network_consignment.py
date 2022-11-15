import unittest

from src.main.upn.api.mapping.network_consignment \
    import NetworkConsignmentConversion

from src.main.upn.api.data_structures.network_consignment.structure \
    import NetworkConsignment

from src.main.freight.consignment.model import Consignment

from src.test.upn.api.mapping.setup import upn_setup


class TestNetworkConsignmentMapping(unittest.TestCase):
    def setUp(self):
        self._network_consignment = upn_setup._dummy_network_consignment()
        # self._correct_freight_consignment = setup.dummy_freight_consignment()

    def test_should_map_network_consignment_to_house_consignment(self):
        self.fail("DUMMY FAIL")


if __name__ == '__main__':
    unittest.main()
