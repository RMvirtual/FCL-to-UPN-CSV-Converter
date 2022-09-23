import unittest
from src.main.file_system.runfiles import load_path
from src.main.forward_office.dashboard.formats import DashboardFormats
from src.main.forward_office.dashboard.export.file_formats import csv


class TestConsignmentParser(unittest.TestCase):
    def setUp(self) -> None:
        dashboard_formats = DashboardFormats()

        read_parameters = csv.ReadParameters()
        read_parameters.csv_path = self._simple_scenario_csv
        read_parameters.dashboard_format = dashboard_formats.UPNEDIIMP
        read_parameters.ignore_headers = True

        self._consignments = csv.read(read_parameters)

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
