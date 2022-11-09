import unittest
from src.main.upn.api.parser.network_pallet import NetworkPalletParser


class TestNetworkPalletParser(unittest.TestCase):
    def setUp(self):
        self._parser = NetworkPalletParser()

    def test_should_parse_network_pallet(self):
        self.fail("DUMMY NETWORK PALLET FAIL")


if __name__ == '__main__':
    unittest.main()

