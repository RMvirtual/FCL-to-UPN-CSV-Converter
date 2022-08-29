import unittest
from rules_python.python.runfiles import runfiles


class TestPackageTypesJsonReader(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_should_read_correct_number_of_fields(self):
        self.fail("Dummy fail on package type json reader.")

    @property
    def _test_json_file(self) -> str:
        r = runfiles.Create()

        return r.Rlocation(
            "fcl-to-upn-csv/resources/test_inputs/base_packages.json")


if __name__ == '__main__':
    unittest.main()
