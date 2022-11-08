import unittest
from src.main.upn.api.structures.network_consignment.structure import \
    NetworkConsignment
from src.main.upn.api.structures.network_pallet.structure import NetworkPallet


class TestNetworkConsignment(unittest.TestCase):
    def setUp(self) -> None:
        pass

    @unittest.SkipTest
    def test_should_create_fields(self):
        structure = NetworkConsignment()

        self.assertTrue(hasattr(structure, "consignment_no"))
        self.assertIsInstance(structure.consignment_no, str)

    def test_should_create_empty_pallets_list(self):
        structure = NetworkConsignment()
        self.assertListEqual([], structure.pallets)

    def test_should_get_data_structure_field_type(self):
        field_type = network_consignment.get_field_type("network_pallet")
        self.assertEqual(NetworkPallet, field_type)

    def test_should_get_array_structure_field_type(self):
        field_type = network_consignment.get_field_type(
            "array_of_network_pallet")

        self.assertEqual(list[NetworkPallet], field_type)


if __name__ == '__main__':
    unittest.main()
