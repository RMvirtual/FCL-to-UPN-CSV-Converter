import unittest

from src.main.freight.consignment.validation \
    import ConsignmentValidationStrategy


class TestConsignmentValidation(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_should_invalidate_incorrect_post_code(self):
        self.fail("DUMMY FAIL FOR CONSIGNMENT INTEGRATION VALIDATION.")


if __name__ == '__main__':
    unittest.main()
