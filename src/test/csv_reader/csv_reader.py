import unittest
from rules_python.python.runfiles import runfiles


class TestCsvReader(unittest.TestCase):
    def test_should_get_number_of_rows(self):
        r = runfiles.Create()
        location = r.Rlocation(
            "fcl-to-upn-csv/resources/test_inputs/simple_scenario.csv")

        print("Location:", location)

        self.fail("FAIL ME")


if __name__ == '__main__':
    unittest.main()
