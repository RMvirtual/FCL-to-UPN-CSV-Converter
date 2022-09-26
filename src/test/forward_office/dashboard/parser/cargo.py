import unittest
from src.main.forward_office.dashboard.parser.cargo import CargoParser


class TestCargoEntryParser(unittest.TestCase):
    def setUp(self) -> None:
        self._dashboard_format = {
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

    def _load_simple_example(self):
        self._dashboard_input = [
            "Mr Susan Cheshire", "10 BRAMBLING RISE",
            "HEMEL HEMPSTEAD", "", "", "HEMEL HEMPSTEAD", "HP2 6DT",
            "GR220806951", "(078)41332424",
            "1000", "1", "PAL2", "PALLETS N/D",
            "PROP PAL LTD",
            "", "", "", "",
            "", "", "", "",
            "", "", "", "",
            "TEL: 07841 332424, TAIL LIFT", "",
            "", "23-Aug-22", "", "1", "2", "Yes"
        ]

    def _load_complex_example(self):
        self._dashboard_input = [
            "Mr Susan Cheshire", "10 BRAMBLING RISE",
            "HEMEL HEMPSTEAD", "", "", "HEMEL HEMPSTEAD", "HP2 6DT",
            "GR220806951", "(078)41332424",
            "2000", "2", "PALL", "PALLETS N/D",
            "PROP PAL LTD",
            "600", "2", "QPL3", "",
            "800", "8", "MPAL", "",
            "1000", "2", "HPL2", "",
            "TEL: 07841 332424, TAIL LIFT", "",
            "", "23-Aug-22", "", "1", "2", "Yes"
        ]

    def test_should_parse_one_cargo_line(self):
        self._load_simple_example()
        parser = CargoParser(self._dashboard_format)
        parser.parse(self._dashboard_input)
        cargo = parser.cargo

        self.assertEqual(1, len(cargo))

        entry = cargo[0]
        self.assertEqual(1, entry.quantity)

        self.assertEqual("pallet", entry.package_type.base_type)
        self.assertEqual("full", entry.package_type.name)
        self.assertEqual(1000, entry.weight_kgs)
        self.assertEqual("double", entry.package_type.oversize_option)

    def test_should_find_missing_weight_error(self):
        self._load_simple_example()
        self._dashboard_input[9] = 0

        parser = CargoParser(self._dashboard_format)

        with self.assertRaises(ValueError):
            parser.parse(self._dashboard_input)

        self.assertEqual(0, len(parser.cargo))
        self.assertEqual(1, len(parser.errors))
        self.assertTrue(parser.errors.weight_incorrect)

    def test_should_find_missing_quantity_and_package_type_errors(self):
        self._load_simple_example()
        self._dashboard_input[10] = 0
        self._dashboard_input[11] = 0

        parser = CargoParser(self._dashboard_format)

        try:
            parser.parse(self._dashboard_input)

        except ValueError as error:
            errors = error.args

        print(errors)

        self.assertEqual(0, len(parser.cargo))
        self.assertEqual(2, len(errors))
        self.assertFalse(errors.weight_incorrect)
        self.assertTrue(errors.blank_package_type)
        self.assertTrue(errors.invalid_quantity)

    def test_should_parse_four_different_cargo_lines(self):
        self._load_complex_example()
        parser = CargoParser(self._dashboard_format)
        parser.parse(self._dashboard_input)
        cargo = parser.cargo

        self.assertEqual(4, len(cargo))

        entry_1 = cargo[0]
        self.assertEqual(2, entry_1.quantity)
        self.assertEqual("pallet", entry_1.package_type.base_type)
        self.assertEqual("full", entry_1.package_type.name)
        self.assertEqual(2000, entry_1.weight_kgs)
        self.assertEqual("normal", entry_1.package_type.oversize_option)

        entry_2 = cargo[1]
        self.assertEqual(2, entry_2.quantity)
        self.assertEqual("pallet", entry_2.package_type.base_type)
        self.assertEqual("quarter", entry_2.package_type.name)
        self.assertEqual(600, entry_2.weight_kgs)
        self.assertEqual("triple", entry_2.package_type.oversize_option)

        entry_3 = cargo[2]
        self.assertEqual(8, entry_3.quantity)
        self.assertEqual("pallet", entry_3.package_type.base_type)
        self.assertEqual("micro", entry_3.package_type.name)
        self.assertEqual(800, entry_3.weight_kgs)
        self.assertEqual("normal", entry_3.package_type.oversize_option)

        entry_4 = cargo[3]
        self.assertEqual(2, entry_4.quantity)
        self.assertEqual("pallet", entry_4.package_type.base_type)
        self.assertEqual("half", entry_4.package_type.name)
        self.assertEqual(1000, entry_4.weight_kgs)
        self.assertEqual("double", entry_4.package_type.oversize_option)


if __name__ == '__main__':
    unittest.main()
