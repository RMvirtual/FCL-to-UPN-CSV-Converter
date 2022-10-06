import unittest

from src.main.freight.consignment.validation \
    import ConsignmentValidationStrategy, ConsignmentErrors

from src.main.freight.consignment.model import Consignment
from src.main.freight.cargo import types


class TestConsignmentValidation(unittest.TestCase):
    def setUp(self):
        self._validation = ConsignmentValidationStrategy()
        self._load_basic_consignment()

    def _load_basic_consignment(self):
        self._consignment = Consignment()
        self._consignment.address.name = "Ryan Matfen"
        self._consignment.address.line_1 = "Gillibrands Road"
        self._consignment.address.town = "Skelmersdale"
        self._consignment.address.post_code = "WN8 9TA"

        self._consignment.service.priority()

        self._consignment.reference = "GR221000100"
        self._consignment.client_name = "UPN"
        self._consignment.delivery_date = "23/10/2022"

        self._consignment.cargo.entry_by_package_type(
            types.load_package_type("full"))

    def test_should_highlight_tail_lift_advisory(self):
        danger_instructions = [
            "Tail lift req", "TL required", "needs t/l",
            "Give meeee a T/L", "customer requires t-lift",
            "send tail-lift"
        ]

        for instruction in danger_instructions:
            errors = self._tail_lift_errors_from_instruction(instruction)
            self.assertTrue(errors.tail_lift_advisory, msg=instruction)

    def test_should_not_highlight_tail_lift_advisory(self):
        errors = self._validation.validate_tail_lift_error(self._consignment)

        self.assertFalse(errors.tail_lift_advisory)

    def _tail_lift_errors_from_instruction(
            self, instruction: str) -> ConsignmentErrors:
        self._consignment.delivery_instructions.clear()
        self._consignment.delivery_instructions.append(instruction)

        return self._validation.validate_tail_lift_error(self._consignment)


if __name__ == '__main__':
    unittest.main()
