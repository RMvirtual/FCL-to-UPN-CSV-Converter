import unittest

from src.main.forward_office.dashboard.export.parser.cargo import CargoParser
from src.main.freight.cargo.types import PackageType


class TestCargoEntryParser(unittest.TestCase):
    def setUp(self) -> None:
        self._field_indexes = {
            "line_1_weight": 9,
            "line_1_quantity": 10,
            "line_1_package_type": 11,
            "line_1_description": 12,
            "line_2_weight": 14,
            "line_2_quantity": 15,
            "line_2_package_type": 16,
            "line_2_description": 17,
            "line_3_weight": 18,
            "line_3_quantity": 19,
            "line_3_package_type": 20,
            "line_3_description": 21,
            "line_4_weight": 22,
            "line_4_quantity": 23,
            "line_4_package_type": 24,
            "line_4_description": 25
        }

        self._values_to_parse = [
            "Mr Susan Cheshire", "10 BRAMBLING RISE", "HEMEL HEMPSTEAD",
            "", "", "HEMEL HEMPSTEAD", "HP2 6DT", "GR220806951",
            "(078)41332424", "1000", "1", "PALL", "PALLETS N/D",
            "PROP PAL LTD", "", "", "", "", "", "", "", "", "", "", "", "",
            "TEL: 07841 332424, TAIL LIFT", "", "", "23-Aug-22", "", "1",
            "2", "Yes"
        ]

    def test_should_parse_one_cargo_entry(self):
        parser = CargoParser(self._field_indexes)
        cargo = parser.parse(self._values_to_parse)

        self.assertEqual(1, len(cargo))

        entry = cargo[0]
        self.assertEqual(1, entry.quantity)
        self.assertEqual(PackageType, entry.package_type)
        self.assertEqual(1000, entry.weight_kgs)


if __name__ == '__main__':
    unittest.main()
