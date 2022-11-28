import unittest

from src.main.companies.forward_office.references.consignment.reference \
    import FCLConsignmentReference


class TestFCLConsignmentReference(unittest.TestCase):
    def test_should_set_full_reference(self):
        reference = str(FCLConsignmentReference("GR220806951"))
        correct_reference = "GR220806951"

        self.assertEqual(correct_reference, reference)

    def test_should_set_numeric_only_reference(self):
        reference = str(FCLConsignmentReference("220806951"))
        correct_reference = "GR220806951"

        self.assertEqual(correct_reference, reference)

    def test_should_error_if_incorrect_prefix(self):
        with self.assertRaises(ValueError):
            _ = FCLConsignmentReference("FE220806951")

    def test_should_error_if_too_few_digits(self):
        with self.assertRaises(ValueError):
            _ = FCLConsignmentReference("GR220806")

    def test_should_error_if_too_many_digits(self):
        with self.assertRaises(ValueError):
            _ = FCLConsignmentReference("2208069510")


if __name__ == '__main__':
    unittest.main()
