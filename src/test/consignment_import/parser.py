import unittest
from rules_python.python.runfiles import runfiles
import src.main.consignment_import.parser.consignment as consignment_parser

class TestConsignmentParser(unittest.TestCase):
    def setUp(self) -> None:
        self._consignments = consignment_parser.read(
            csv_path=self._simple_scenario_csv,
            ignore_headers=True,
            file_format=UpnEdiImp()
        )

    def test_should_read_a_quantity_of_one_consignment(self):
        self.assertEqual(1, len(self._consignments))

    def test_should_read_a_consignment_reference(self):
        reference = list(self._consignments.values())[0].reference
        self.assertEqual(reference, "GR220806951")

    def test_should_read_a_consignment_address(self):
        address = list(self._consignments.values())[0].address
        self.assertEqual(address.name, "10 BRAMBLING RISE")
        self.assertEqual(address.line_1, "HEMEL HEMPSTEAD")
        self.assertEqual(address.line_2, "")
        self.assertEqual(address.line_3, "")
        self.assertEqual(address.town, "HEMEL HEMPSTEAD")
        self.assertEqual(address.post_code, "HP2 6DT")
        self.assertEqual(address.country, "GB")
        self.assertEqual(address.contact_name, "Mr Susan Cheshire")
        self.assertEqual(address.telephone_number, "(078) 4133 2424")

    def test_should_get_one_cargo_entry_from_description(self):
        cargo = list(
            self._consignments.values())[0].cargo

        self.assertEqual(1, len(cargo))

    @property
    def _simple_scenario_csv(self) -> str:
        r = runfiles.Create()

        return r.Rlocation(
            "fcl-to-upn-csv/resources/test_inputs/simple_scenario.csv")


if __name__ == '__main__':
    unittest.main()
