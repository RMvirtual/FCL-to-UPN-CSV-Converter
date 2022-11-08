import unittest
from src.main.upn.api.structures import network_consignment
from src.main.upn.api.structures.network_pallet import NetworkPallet


class TestNetworkConsignment(unittest.TestCase):
    def setUp(self) -> None:
        pass

    @unittest.SkipTest
    def test_should_create_fields(self):
        ...
        # structure = NetworkConsignment()

        # self.assertTrue(hasattr(structure, "consignment_no"))
        # self.assertIsInstance(structure.consignment_no, str)

    def test_should_get_data_structure(self):
        structure = network_consignment.get_data_structure("network_pallet")
        self.assertEqual(NetworkPallet, structure)

    def test_should_extract_underlying_array_object_type(self):
        result = network_consignment.extract_array_object_name(
            "array_of_network_pallet")

        self.assertEqual("network_pallet", result)

    def test_should_get_field_type_of_primitive(self):
        field_type = network_consignment.get_field_type("string")
        self.assertEqual(str, field_type)

    def test_should_get_field_type_of_data_structure(self):
        field_type = network_consignment.get_field_type("network_pallet")
        self.assertEqual(NetworkPallet, field_type)

    def test_should_get_field_type_of_array(self):
        field_type = network_consignment.get_field_type(
            "array_of_network_pallet")

        self.assertEqual(list[NetworkPallet], field_type)


if __name__ == '__main__':
    unittest.main()
