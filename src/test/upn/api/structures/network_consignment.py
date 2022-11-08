import unittest
from src.main.upn.api.structures.network_consignment import NetworkConsignment


class TestNetworkConsignment(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_should_create_fields(self):
        structure = NetworkConsignment()

        self.assertTrue(hasattr(structure, "consignment_no"))
        self.assertIsInstance(structure.consignment_no, str)


if __name__ == '__main__':
    unittest.main()
