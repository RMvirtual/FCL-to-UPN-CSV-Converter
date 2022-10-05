import unittest
from src.main.forward_office.dashboard.parser.model.cargo import CargoParser

from src.main.forward_office.dashboard.parser.requests.types \
    import CargoParseRequest, CargoEntryParseRequest


class TestCargoParser(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def _load_simple_example(self):
        self._example = CargoParseRequest()

        self._example.line_1 = CargoEntryParseRequest()
        self._example.line_1.package_type = "PAL2"
        self._example.line_1.quantity = "1"
        self._example.line_1.weight = "1000"
        self._example.line_1.goods_description = "PALLETS N/D"

    def _load_complex_example(self):
        self._example = CargoParseRequest()

        self._example.line_1 = CargoEntryParseRequest()
        self._example.line_1.package_type = "PALL"
        self._example.line_1.quantity = "2"
        self._example.line_1.weight = "2000"
        self._example.line_1.goods_description = "PALLETS N/D"

        self._example.line_2 = CargoEntryParseRequest()
        self._example.line_2.package_type = "QPL3"
        self._example.line_2.quantity = "2"
        self._example.line_2.weight = "600"
        self._example.line_2.goods_description = "TRIPLE QUARTER PALLET"

        self._example.line_3 = CargoEntryParseRequest()
        self._example.line_3.package_type = "MPAL"
        self._example.line_3.quantity = "8"
        self._example.line_3.weight = "800"
        self._example.line_3.goods_description = "MICRO PALLET"

        self._example.line_4 = CargoEntryParseRequest()
        self._example.line_4.package_type = "HPL2"
        self._example.line_4.quantity = "2"
        self._example.line_4.weight = "1000"
        self._example.line_4.goods_description = "DOUBLE HALF PALLET"

    def test_should_parse_one_cargo_line(self):
        self._load_simple_example()

        parser = CargoParser()
        cargo = parser.parse(self._example)

        self.assertEqual(1, len(cargo))

        entry = cargo[0]
        self.assertEqual(1, entry.quantity)

        self.assertEqual("pallet", entry.package_type.base_type)
        self.assertEqual("full", entry.package_type.name)
        self.assertEqual(1000, entry.weight_kgs)
        self.assertEqual("double", entry.package_type.oversize_option)

    def test_should_parse_four_different_cargo_lines(self):
        self._load_complex_example()

        parser = CargoParser()
        cargo = parser.parse(self._example)

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
