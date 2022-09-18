import unittest
from src.main.file_system.runfiles import load_path
from src.main.forward_office.dashboard.export import upn_edi_imp_csv


class TestConsignmentParser(unittest.TestCase):
    def setUp(self) -> None:
        self._consignments = upn_edi_imp_csv.import_upn_edi_imp_csv_fcl_export(
            csv_path=self._simple_scenario_csv)

    def test_should_read_a_quantity_of_one_consignment(self):
        self.assertEqual(1, len(self._consignments))

    def test_should_read_a_consignment_reference(self):
        reference = list(self._consignments.values())[0].reference
        self.assertEqual(reference, "GR220806951")

    def test_should_read_a_consignment_address(self):
        address = list(self._consignments.values())[0].address
        self.assertEqual(address.name, "10 BRAMBLING RISE")
        self.assertEqual(address.line_1, "HEMEL HEMPSTEAD")
        self.assertEqual(address.line_2, "")
        self.assertEqual(address.line_3, "")
        self.assertEqual(address.town, "HEMEL HEMPSTEAD")
        self.assertEqual(address.post_code, "HP2 6DT")
        self.assertEqual(address.country, "GB")
        self.assertEqual(address.contact_name, "Mr Susan Cheshire")
        self.assertEqual(address.telephone_number, "(078) 4133 2424")

    def test_should_read_correct_number_of_cargo_entries(self):
        consignment = list(self._consignments.values())[0]
        cargo = consignment.cargo
        self.assertEqual(1, len(cargo))

    @property
    def _simple_scenario_csv(self) -> str:
        return load_path("resources/test_inputs/simple_scenario.csv")


if __name__ == '__main__':
    unittest.main()
