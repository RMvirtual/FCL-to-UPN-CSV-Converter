import unittest

from src.main.upn.api.adaptors.network_consignment \
    import NetworkConsignmentAdapter

from src.test.upn.api.adaptors.network_consignment.setup import (
    graylaw_setup, upn_setup)


class TestNetworkConsignmentAdaptor(unittest.TestCase):
    def setUp(self):
        self._network_consignment = upn_setup.dummy_network_consignment()
        self._correct_graylaw_consignment = graylaw_setup.dummy_consignment()

    def test_should_adapt_network_consignment(self) -> None:
        adaptor = NetworkConsignmentAdapter(self._network_consignment)



if __name__ == '__main__':
    unittest.main()
