import unittest
import src.main.csv.reader as csv_reader
from rules_python.python.runfiles import runfiles


class TestCsvReader(unittest.TestCase):
    def setUp(self) -> None:
        self._load_csv_file()
        self._initialise_correct_headers()

    def test_should_get_number_of_rows(self):
        rows = self._csv_file.number_of_rows()
        correct_no_of_rows = 2

        self.assertEqual(correct_no_of_rows, rows)

    def test_should_read_first_line_headers(self):
        headers = self._csv_file.at(0)
        self.assertListEqual(self._correct_headers, headers)

    def _load_csv_file(self) -> None:
        r = runfiles.Create()

        location = r.Rlocation(
            "fcl-to-upn-csv/resources/test_inputs/simple_scenario.csv")

        self._csv_file = csv_reader.read(location)

    def _initialise_correct_headers(self) -> None:
        self._correct_headers = [
            "ContactName", "CompanyName", "StreetName", "Locality",
            "Town", "County", "Postcode", "ConNo",
            "ContactPhone",
            "Weight1", "Pkgs.1", "Pkg Type1", "Gds.Desc1",
            "Client",
            "Weight2", "Pkgs.2", "Pkg Type2", "Gds.Desc2",
            "Weight3", "Pkgs.3", "Pkg Type3", "Gds.Desc3",
            "Weight4", "Pkgs.4", "Pkg Type4", "Gds.Desc4",
            "SpecInstr:1:", "SpecInstr:2:", "BI Time", "DelDate",
            "CustRef", "Pallets", "DelService", "Tail Lift Del"
        ]


if __name__ == '__main__':
    unittest.main()
