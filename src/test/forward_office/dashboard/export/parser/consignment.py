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

    @property
    def _simple_scenario_csv(self) -> str:
        return load_path("resources/test_inputs/simple_scenario.csv")


if __name__ == '__main__':
    unittest.main()
