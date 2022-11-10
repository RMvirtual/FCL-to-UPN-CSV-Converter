import unittest
from src.main.upn.api.data_structures import data_structures
from src.main.upn.api.data_structures.network_pallet.structure import NetworkPallet


class TestUpnDataStructures(unittest.TestCase):
    def test_should_get_data_structure(self):
        structure = data_structures.get_data_structure("network_pallet")
        self.assertEqual(NetworkPallet, structure)

    def test_should_detect_field_type_as_data_structure(self):
        self.assertTrue(data_structures.is_data_structure("network_pallet"))

        self.assertFalse(
            data_structures.is_data_structure("array_of_network_pallet"))


if __name__ == '__main__':
    unittest.main()
