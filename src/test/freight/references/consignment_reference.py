import unittest
from src.main.freight.references.model import ConsignmentReference


class TestConsignmentReference(unittest.TestCase):
    def test_should_set_full_reference(self):
        correct_reference = "GR220806951"
        reference = str(ConsignmentReference("GR220806951"))

        self.assertEqual(correct_reference, reference)

    def test_should_set_numeric_only_reference(self):
        correct_reference = "GR220806951"
        reference = str(ConsignmentReference("220806951"))

        self.assertEqual(correct_reference, reference)

    def test_should_error_if_incorrect_prefix(self):
        with self.assertRaises(ValueError):
            _ = ConsignmentReference("FE220806951")

    def test_should_error_if_too_few_digits(self):
        with self.assertRaises(ValueError):
            _ = ConsignmentReference("GR220806")

    def test_should_error_if_too_many_digits(self):
        with self.assertRaises(ValueError):
            _ = ConsignmentReference("2208069510")


if __name__ == '__main__':
    unittest.main()
