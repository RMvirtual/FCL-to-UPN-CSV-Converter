import unittest
from src.main.companies.upn.database.services import UPNServicesDatabase


class TestUPNServicesDatabase(unittest.TestCase):
    def setUp(self):
        self._database = UPNServicesDatabase()

    def test_should_get_main_service_for_network_consignment(self) -> None:
        result = self._database.main_service()

        self.assertListEqual(["P", "S", "I", "R"], result.constraints())
        self.assertEqual("P", result.selection)


if __name__ == '__main__':
    unittest.main()
