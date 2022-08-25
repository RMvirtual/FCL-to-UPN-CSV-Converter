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
        line_2.number_of_pallets = 1
        line_2.total_weight = 500

        cargo = Cargo()
        cargo.add(line_1)
        cargo.add(line_2)

        self.assertEqual(len(cargo), 1)


if __name__ == '__main__':
    unittest.main()
