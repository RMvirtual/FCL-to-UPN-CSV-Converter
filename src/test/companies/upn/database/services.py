import unittest
from src.main.companies.upn.database.services import UPNServicesDatabase


class TestUPNServicesDatabase(unittest.TestCase):
    def setUp(self):
        self._database = UPNServicesDatabase()

    def test_should_get_main_service_for_network_consignment(self) -> None:
        result = self._database.main_service()

        self.assertListEqual(["P", "S", "I", "R"], result.constraints())
        self.assertEqual("P", result.selection)

    def test_should_get_premium_service_for_network_consignment(self) -> None:
        result = self._database.premium_service()

        self.assertListEqual(
            ["", "B10", "AM", "Timed", "Sat"], result.constraints())
        self.assertEqual("", result.selection)

    def test_should_get_tail_lift_service_for_network_consignment(
            self) -> None:
        result = self._database.tail_lift_required()

        self.assertListEqual(["", "TLift"], result.constraints())
        self.assertEqual("", result.selection)

    def test_should_get_additional_service_for_network_consignment(
            self) -> None:
        result = self._database.additional_service()

        self.assertListEqual(["", "BI", "Bkd", "OOH"], result.constraints())
        self.assertEqual("", result.selection)


if __name__ == '__main__':
    unittest.main()
