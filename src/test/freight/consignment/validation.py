import unittest

from src.main.freight.consignment.validation \
    import ConsignmentValidationStrategy

from src.main.freight.consignment.model import Consignment
from src.main.freight.cargo import types


class TestConsignmentValidation(unittest.TestCase):
    def _load_basic_consignment(self):
        self._consignment = Consignment()
        self._consignment.address.name = "Ryan Matfen"
        self._consignment.address.line_1 = "Gillibrands Road"
        self._consignment.address.town = "Skelmersdale"
        self._consignment.address.post_code = "WN8 9TA"

        self._consignment.service.priority()
        self._consignment.service.tail_lift()

        self._consignment.reference = "GR221000100"
        self._consignment.client_name = "UPN"
        self._consignment.delivery_instructions.append("Tail Lift")
        self._consignment.delivery_date = "23/10/2022"

        self._consignment.cargo.entry_by_package_type(
            types.load_package_type("full"))

    def test_should_highlight_tail_lift_advisory(self):
        validation = ConsignmentValidationStrategy()
        errors = validation.validate_tail_lift_error(self._consignment)

        self.assertTrue(errors.tail_lift_advisory)


if __name__ == '__main__':
    unittest.main()
