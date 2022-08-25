import unittest
from src.main.consignment.cargo.entry import CargoEntry
from src.main.consignment.cargo.types import *
from src.main.consignment.cargo.model import Cargo


class TestCargo(unittest.TestCase):
    def test_should_add_a_single_cargo_entry(self):
        cargo_line = CargoEntry()
        cargo_line.pallet_type = FullPallet()
        cargo_line.number_of_pallets = 1
        cargo_line.total_weight = 1000

        cargo = Cargo()
        cargo.add(cargo_line)

        self.assertIsInstance(cargo[0].pallet_type, FullPallet)
        self.assertEqual(cargo[0].number_of_pallets, 1)
        self.assertEqual(cargo[0].total_weight, 1000)

    def test_should_combine_two_cargo_entries(self):
        line_1 = CargoEntry()
        line_1.pallet_type = HalfPallet()
        line_1.number_of_pallets = 1
        line_1.total_weight = 400

        line_2 = CargoEntry()
        line_2.pallet_type = HalfPallet()
        line_2.number_of_pallets = 2
        line_2.total_weight = 1000

        cargo = Cargo()
        cargo.add(line_1)
        cargo.add(line_2)

        correct_no_of_entries = 1
        correct_total_weight = 1400
        correct_total_pallets = 3

        self.assertEqual(correct_no_of_entries, len(cargo))
        self.assertEqual(correct_total_pallets, cargo[0].number_of_pallets)
        self.assertEqual(correct_total_weight, cargo[0].total_weight)
        self.assertIsInstance(cargo[0].pallet_type, HalfPallet)

    def test_should_reject_combining_two_cargo_entries(self):
        line_1 = CargoEntry()
        line_1.pallet_type = HalfPallet()
        line_1.number_of_pallets = 1
        line_1.total_weight = 400

        line_2 = CargoEntry()
        line_2.pallet_type = FullPallet()
        line_2.number_of_pallets = 1
        line_2.total_weight = 1000

        with self.assertRaises(ValueError):
            line_1 += line_2

    def test_should_add_two_different_pallet_types(self):
        line_1 = CargoEntry()
        line_1.pallet_type = HalfPallet()
        line_1.number_of_pallets = 1
        line_1.total_weight = 400

        line_2 = CargoEntry()
        line_2.pallet_type = FullPallet()
        line_2.number_of_pallets = 3
        line_2.total_weight = 1000

        cargo = Cargo()
        cargo.add(line_1)
        cargo.add(line_2)

        self.assertEqual(2, len(cargo))

        self.assertEqual(1, cargo[0].number_of_pallets)
        self.assertEqual(400, cargo[0].total_weight)
        self.assertIsInstance(cargo[0].pallet_type, HalfPallet)

        self.assertEqual(3, cargo[1].number_of_pallets)
        self.assertEqual(1000, cargo[1].total_weight)
        self.assertIsInstance(cargo[1].pallet_type, FullPallet)


if __name__ == '__main__':
    unittest.main()
