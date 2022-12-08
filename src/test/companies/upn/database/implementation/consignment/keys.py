import unittest
from src.main.companies.upn.database.consignment.network.keys \
    import NetworkConsignmentKeys


class TestNetworkConsignmentKeys(unittest.TestCase):
    def setUp(self):
        self._key_map = NetworkConsignmentKeys()

    def test_should_load_network_consignment_key_mappings(self) -> None:
        self.assertEqual("Depot", self._key_map.depot_no)


if __name__ == "__main__":
    unittest.main()
