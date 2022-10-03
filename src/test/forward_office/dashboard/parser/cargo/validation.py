import unittest
from src.main.forward_office.dashboard.parser.cargo.validation \
    import CargoEntryParseValidator


class TestCargoEntryParser(unittest.TestCase):
    def test_should_find_missing_weight_error(self):
        validator = CargoEntryParseValidator()
        errors = validator.find_errors("PALL", "1", "")
        self.assertEqual(1, len(errors))
        self.assertTrue(errors.weight_incorrect)

    def test_should_find_missing_quantity_and_package_type_errors(self):
        validator = CargoEntryParseValidator()
        errors = validator.find_errors("", "", "1000")
        self.assertEqual(2, len(errors))
        self.assertFalse(errors.weight_incorrect)
        self.assertTrue(errors.blank_package_type)
        self.assertTrue(errors.invalid_quantity)


if __name__ == '__main__':
    unittest.main()
