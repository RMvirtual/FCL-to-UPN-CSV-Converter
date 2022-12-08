import unittest
from src.main.file_system.companies.upn.api.consignments.network \
    import NetworkConsignmentFiles


class TestUPNConsignmentFiles(unittest.TestCase):
    def setUp(self) -> None:
        self._files = NetworkConsignmentFiles()

    def test_can_load_upn_network_consignment_keys(self) -> None:
        self.assertEqual("ConBarcode", self._files.keys["barcode"])

    def test_can_load_upn_network_consignment_constraints(self) -> None:
        self.assertDictEqual(
            {"type": "string", "values": ["P", "S", "I", "R"]},
            self._files.constraints["MainService"]
        )


if __name__ == '__main__':
    unittest.main()
