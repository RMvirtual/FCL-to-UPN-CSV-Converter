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

    def test_should_populate_fields(self):
        structure = upn.NetworkConsignment().consignment_no

        self.assertEqual(structure.type, "string")
        self.assertEqual(structure.mapping, "ConNo")


if __name__ == '__main__':
    unittest.main()
