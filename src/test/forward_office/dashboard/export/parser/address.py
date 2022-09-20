import unittest

from src.main.file_system.runfiles import load_path
from src.main.forward_office.dashboard.export.parser.address \
    import AddressParser


class TestAddressParser(unittest.TestCase):
    def setUp(self) -> None:
        self._fields = {
            "contact_name": 0,
            "company_name": 1,
            "address_line_1": 2,
            "address_line_2": 3,
            "address_line_3": 4,
            "town": 5,
            "post_code": 6,
            "telephone_no": 8
        }

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

    @property
    def _simple_scenario_csv(self) -> str:
        return load_path("resources/test_inputs/simple_scenario.csv")


if __name__ == '__main__':
    unittest.main()
