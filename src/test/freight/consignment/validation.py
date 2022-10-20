import unittest

from src.main.freight.consignment.validation import (
    ConsignmentValidationStrategy, ConsignmentErrors)

from src.main.freight.consignment.model import Consignment
from src.main.freight.cargo import package_types


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
        self._consignment.shipment_dates.collection_date = "03/10/2022"
        self._consignment.shipment_dates.delivery_date = "04/10/2022"

        self._consignment.cargo.entry_by_package_type(
            package_types.load("full"))

    def test_should_highlight_tail_lift_errors(self):
        tail_lift_instructions = [
            "Tail lift req", "TL required", "needs t/l",
            "Give meeee a T/L", "customer requires t-lift",
            "send tail-lift" "TL"
        ]

        for instruction in tail_lift_instructions:
            errors = self._tail_lift_errors_from_instruction(instruction)
            self.assertTrue(errors.tail_lift_advisory, msg=instruction)

    def test_should_avoid_false_positive_tail_lift_errors(self):
        false_positives = [
            "reference: fat/lad", "also reference: fat /lad",
            "ATTL64", "battle"
        ]

        for instruction in false_positives:
            errors = self._tail_lift_errors_from_instruction(instruction)
            self.assertFalse(errors.tail_lift_advisory, msg=instruction)

    def _tail_lift_errors_from_instruction(
            self, instruction: str) -> ConsignmentErrors:
        self._consignment.delivery_instructions.clear()
        self._consignment.delivery_instructions.append(instruction)

        return self._validation.validate_tail_lift_error(self._consignment)

    def test_should_approve_priority_date(self):
        errors = self._validation.validate_dates_against_service(
            self._consignment)

        self.assertFalse(errors.incongruent_delivery_date)

    def test_should_highlight_priority_dates_error(self):
        self._consignment.shipment_dates.delivery_date = "05/10/2022"

        errors = self._validation.validate_dates_against_service(
            self._consignment)

        self.assertTrue(errors.incongruent_delivery_date)

    def test_should_highlight_economy_date_error(self):
        self._consignment.service.economy()

        errors = self._validation.validate_dates_against_service(
            self._consignment)

        self.assertTrue(errors.incongruent_delivery_date)

    def test_should_approve_economy_date(self):
        self._consignment.service.economy()
        self._consignment.shipment_dates.delivery_date = "05/10/2022"

        errors = self._validation.validate_dates_against_service(
            self._consignment)

        self.assertFalse(errors.incongruent_delivery_date)

    def test_should_approve_economy_booked_date(self):
        self._consignment.service.economy()
        self._consignment.service.booked()
        self._consignment.shipment_dates.delivery_date = "06/10/2022"

        errors = self._validation.validate_dates_against_service(
            self._consignment)

        self.assertFalse(errors.incongruent_delivery_date)

    def test_should_highlight_economy_booked_date_error(self):
        self._consignment.service.economy()
        self._consignment.service.clear_booked_service()
        self._consignment.shipment_dates.delivery_date = "06/10/2022"

        errors = self._validation.validate_dates_against_service(
            self._consignment)

        self.assertTrue(errors.incongruent_delivery_date)


if __name__ == '__main__':
    unittest.main()
