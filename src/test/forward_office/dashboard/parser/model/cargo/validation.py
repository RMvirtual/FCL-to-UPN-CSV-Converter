import unittest
from src.main.forward_office.dashboard.parser.model.cargo import validation

from src.main.forward_office.dashboard.parser.requests.types \
    import CargoEntryParseRequest


class TestCargoEntryParser(unittest.TestCase):
    def test_should_find_missing_weight_error(self):
        errors = validation.find_errors(
            CargoEntryParseRequest("PALL", "1", ""))

        self.assertEqual(1, len(errors))
        self.assertTrue(errors.weight_incorrect)

    def test_should_find_missing_quantity_and_package_type_errors(self):
        errors = validation.find_errors(
            CargoEntryParseRequest("", "", "1000"))

        self.assertEqual(3, len(errors))
        self.assertTrue(errors.blank_package_type)
        self.assertTrue(errors.invalid_quantity)
        self.assertTrue(errors.invalid_package_type)

    def test_should_raise_invalid_package_type_error(self):
        errors = validation.find_errors(
            CargoEntryParseRequest("LIFT", "1", "1000"))

        self.assertEqual(1, len(errors))
        self.assertTrue(errors.invalid_package_type)


if __name__ == '__main__':
    unittest.main()
