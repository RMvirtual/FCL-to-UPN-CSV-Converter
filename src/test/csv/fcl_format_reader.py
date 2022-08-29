import unittest
from rules_python.python.runfiles import runfiles


class TestFclFormatReader(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_should_read_format_file_into_dictionary(self):
        self.fail("Dummy fail for fcl format reader.")

    @property
    def _test_json_file(self) -> str:
        r = runfiles.Create()

        return r.Rlocation(
            "fcl-to-upn-csv/resources/test_inputs/upn_edi_imp.json")


if __name__ == '__main__':
    unittest.main()
