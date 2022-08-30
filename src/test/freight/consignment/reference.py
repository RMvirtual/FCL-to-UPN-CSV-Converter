import unittest
from src.main.freight.consignment.reference import Reference


class TestReference(unittest.TestCase):
    def test_should_set_full_reference(self):
        correct_reference = "GR220806951"
        reference = str(Reference("GR220806951"))

        self.assertEqual(correct_reference, reference)

    def test_should_set_numeric_only_reference(self):
        correct_reference = "GR220806951"
        reference = Reference("220806951").string()

        self.assertEqual(correct_reference, reference)

    def test_should_error_if_incorrect_prefix(self):
        with self.assertRaises(ValueError):
            _ = Reference("FE220806951")

    def test_should_error_if_too_few_digits(self):
        with self.assertRaises(ValueError):
            _ = Reference("GR220806")

    def test_should_error_if_too_many_digits(self):
        with self.assertRaises(ValueError):
            _ = Reference("2208069510")


if __name__ == '__main__':
    unittest.main()
