import unittest
from src.main.consignment.cargo.entry import CargoEntry
from src.main.consignment.cargo.types import *


class TestCargoEntry(unittest.TestCase):
    def test_should_create_cargo_entry(self):
        cargo_line = CargoEntry()
        cargo_line.pallet_type = FullPallet()
        cargo_line.number_of_pallets = 1
        cargo_line.total_weight = 1000


        self.fail("Force fail on cargo module")


if __name__ == '__main__':
    unittest.main()
