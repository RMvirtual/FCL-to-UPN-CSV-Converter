import unittest
from rules_python.python.runfiles import runfiles
import src.main.csv.fcl_parser as fcl_csv_parser


class TestFclCsvParser(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_should_read_simple_scenario_into_a_consignment(self):
        consignments = fcl_csv_parser.read(self._simple_scenario_csv)

        self.assertEqual(1, len(consignments))

    @property
    def _simple_scenario_csv(self) -> str:
        r = runfiles.Create()

        return r.Rlocation(
            "fcl-to-upn-csv/resources/test_inputs/simple_scenario.csv")


if __name__ == '__main__':
    unittest.main()
