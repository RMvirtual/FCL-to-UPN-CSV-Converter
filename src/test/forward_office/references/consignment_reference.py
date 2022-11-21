import unittest

from src.main.forward_office.references.consignment.reference \
    import FclConsignmentReference


class TestFclConsignmentReference(unittest.TestCase):
    def test_should_set_full_reference(self):
        reference = str(FclConsignmentReference("GR220806951"))
        correct_reference = "GR220806951"

        self.assertEqual(correct_reference, reference)

    def test_should_set_numeric_only_reference(self):
        reference = str(FclConsignmentReference("220806951"))
        correct_reference = "GR220806951"

        self.assertEqual(correct_reference, reference)

    def test_should_error_if_incorrect_prefix(self):
        with self.assertRaises(ValueError):
            _ = FclConsignmentReference("FE220806951")

    def test_should_error_if_too_few_digits(self):
        with self.assertRaises(ValueError):
            _ = FclConsignmentReference("GR220806")

    def test_should_error_if_too_many_digits(self):
        with self.assertRaises(ValueError):
            _ = FclConsignmentReference("2208069510")


if __name__ == '__main__':
    unittest.main()
