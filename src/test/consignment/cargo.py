import unittest
from src.main.consignment.cargo.entry import CargoEntry


class TestCargoEntry(unittest.TestCase):
    def test_should_create_cargo_entry(self):
        cargo_line = CargoEntry()
        cargo_line.pallet_type = None

        self.fail("Force fail on cargo module")


if __name__ == '__main__':
    unittest.main()
