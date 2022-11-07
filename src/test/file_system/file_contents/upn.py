import unittest
from src.main.file_system.file_contents import upn


class TestNetworkConsignmentStruct(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_should_create_fields(self):
        structure = upn.NetworkConsignment()

        self.assertTrue(hasattr(structure, "consignment_no"))
        self.assertTrue(hasattr(structure.consignment_no, "type"))
        self.assertTrue(hasattr(structure.consignment_no, "mapping"))
        self.assertTrue(hasattr(structure.consignment_no, "values"))

    def test_should_populate_field_without_strict_values(self):
        structure = upn.NetworkConsignment().consignment_no

        self.assertEqual(structure.type, "string")
        self.assertEqual(structure.mapping, "ConNo")
        self.assertListEqual(structure.values, [])

    def test_should_populate_field_with_strict_values(self):
        structure = upn.NetworkConsignment().additional_service

        self.assertEqual(structure.type, "string")
        self.assertEqual(structure.mapping, "ExtraService")
        self.assertListEqual(structure.values, ["", "BI", "Bkd", "OOH"])


if __name__ == '__main__':
    unittest.main()
