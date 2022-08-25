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


if __name__ == '__main__':
    unittest.main()
