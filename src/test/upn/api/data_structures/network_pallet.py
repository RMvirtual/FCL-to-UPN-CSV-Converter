import unittest
from src.main.upn.api.data_structures.network_pallet.structure import NetworkPallet


class TestNetworkPallet(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_should_create_fields(self):
        structure = NetworkPallet()

        self.assertTrue(hasattr(structure, "consignment_barcode_no"))
        self.assertTrue(hasattr(structure, "pallet_type"))
        self.assertTrue(hasattr(structure, "pallet_size"))
        self.assertTrue(hasattr(structure, "pallet_barcode_no"))


if __name__ == '__main__':
    unittest.main()
