import unittest
from rules_python.python.runfiles import runfiles
import src.main.csv.fcl_parser as fcl_csv_parser
from src.main.json.fcl_format import UpnEdiImp


class TestFclCsvParser(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_should_read_a_quantity_of_one_consignment(self):
        consignments = fcl_csv_parser.read(
            csv_path=self._simple_scenario_csv,
            ignore_headers=True,
            file_format=UpnEdiImp()
        )

        self.assertEqual(1, len(consignments))

    def test_should_read_a_consignment_reference(self):
        consignments = fcl_csv_parser.read(
            csv_path=self._simple_scenario_csv,
            ignore_headers=True,
            file_format=UpnEdiImp()
        )

        reference = list(consignments.values())[0].reference
        self.assertEqual(reference, "GR220806951")

    def test_should_read_a_consignment_address(self):
        consignments = fcl_csv_parser.read(
            csv_path=self._simple_scenario_csv,
            ignore_headers=True,
            file_format=UpnEdiImp()
        )

        address = list(consignments.values())[0].address
        self.assertEqual(address.name, "10 BRAMBLING RISE")
        self.assertEqual(address.line_1, "HEMEL HEMPSTEAD")
        self.assertEqual(address.line_2, "")
        self.assertEqual(address.line_3, "")
        self.assertEqual(address.town, "HEMEL HEMPSTEAD")
        self.assertEqual(address.post_code, "HP2 6DT")
        self.assertEqual(address.country, "GB")
        self.assertEqual(address.contact_name, "Mr Susan Cheshire")
        self.assertEqual(address.telephone_number, "(078) 4133 2424")

    @property
    def _simple_scenario_csv(self) -> str:
        r = runfiles.Create()

        return r.Rlocation(
            "fcl-to-upn-csv/resources/test_inputs/simple_scenario.csv")


if __name__ == '__main__':
    unittest.main()