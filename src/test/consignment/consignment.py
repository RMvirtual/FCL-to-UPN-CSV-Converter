import unittest
from rules_python.python.runfiles import runfiles


class TestConsignment(unittest.TestCase):
    def setUp(self) -> None:
        self._initialise_csv_path()

    def _initialise_csv_path(self) -> None:
        data_files = runfiles.Create()

        self._csv_path = data_files.Rlocation(
            "fcl-to-upn-csv/resources/test_inputs/simple_scenario.csv")

    def test_should_create_consignment_from_upn_csv(self):
        consignment = Consignment.fromUpnCsv(self._csv_path)

        self.fail("Force fail")


if __name__ == '__main__':
    unittest.main()
