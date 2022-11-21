import unittest
from src.test.upn.api.adaptors.network_consignment.setup import freight_setup, \
    upn_setup


class TestNetworkConsignmentMapping(unittest.TestCase):
    def setUp(self):
        self._network_consignment = upn_setup.dummy_network_consignment()
        self._correct_freight_consignment = freight_setup.dummy_consignment()

    def test_should_convert_network_consignment_into_house_consignment(
            self) -> None:
        self.fail("DUMMY FAIL")


if __name__ == '__main__':
    unittest.main()
