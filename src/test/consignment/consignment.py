import unittest
from rules_python.python.runfiles import runfiles
from src.main.consignment.consignment import Consignment


class TestConsignment(unittest.TestCase):
    def setUp(self) -> None:
        self._initialise_csv_path()
        self._consignment = Consignment()

    def _initialise_csv_path(self) -> None:
        data_files = runfiles.Create()

        self._csv_path = data_files.Rlocation(
            "fcl-to-upn-csv/resources/test_inputs/simple_scenario.csv")

    def test_should_set_full_reference(self):
        correct_reference = "GR220806951"
        self._consignment.reference = "GR220806951"

        self.assertEqual(correct_reference, self._consignment.reference)

    def test_should_set_numeric_only_reference(self):
        correct_reference = "GR220806951"
        self._consignment.reference = "220806951"

        self.assertEqual(correct_reference, self._consignment.reference)

if __name__ == '__main__':
    unittest.main()
