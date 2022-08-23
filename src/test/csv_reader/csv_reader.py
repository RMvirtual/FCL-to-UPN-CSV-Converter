import unittest
import src.main.csv.reader as csv_reader
from rules_python.python.runfiles import runfiles


class TestCsvReader(unittest.TestCase):
    def test_should_get_number_of_rows(self):
        r = runfiles.Create()
        location = r.Rlocation(
            "fcl-to-upn-csv/resources/test_inputs/simple_scenario.csv")

        csv_file = csv_reader.read(location)
        rows = csv_file.number_of_rows()
        correct_no_of_rows = 2

        self.assertEqual(correct_no_of_rows, rows)
        self.assertNotEqual(0, rows)

if __name__ == '__main__':
    unittest.main()
