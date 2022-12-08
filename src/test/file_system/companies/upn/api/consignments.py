import unittest
from src.main.file_system.companies.upn.api.consignments.network \
    import NetworkConsignmentFiles


class TestUPNConsignmentFiles(unittest.TestCase):
    def setUp(self) -> None:
        self._files = NetworkConsignmentFiles()

    def test_can_load_upn_network_pallet_keys(self) -> None:
        self.assertEqual("ConBarcode", self._files.keys["consignment_barcode"])

    def test_can_load_upn_network_pallet_constraints(self) -> None:
        self.assertDictEqual(
            {"type": "string", "values": ["N", "O", "2", "3"]},
            self._files.constraints["PalletSize"]
        )


if __name__ == '__main__':
    unittest.main()
