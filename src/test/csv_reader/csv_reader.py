import unittest
import src.main.csv.reader as csv_reader
from rules_python.python.runfiles import runfiles


class TestCsvReader(unittest.TestCase):
    def setUp(self) -> None:
        self._load_csv_file()

    def test_should_get_number_of_rows(self):
        rows = self._csv_file.number_of_rows()
        correct_no_of_rows = 2

        self.assertEqual(correct_no_of_rows, rows)

    def test_should_read_first_line(self):
        self.fail("Force fail")

    def _load_csv_file(self):
        r = runfiles.Create()
        location = r.Rlocation(
            "fcl-to-upn-csv/resources/test_inputs/simple_scenario.csv")

        self._csv_file = csv_reader.read(location)


if __name__ == '__main__':
    unittest.main()
