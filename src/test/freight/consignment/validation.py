import unittest

from src.main.freight.consignment.validation import (
    ConsignmentValidationStrategy, ConsignmentErrors)

from src.main.freight.consignment.model import Consignment


class TestConsignmentValidation(unittest.TestCase):
    def setUp(self):
        self._validation = ConsignmentValidationStrategy(
            self._setup_consignment())

    @staticmethod
    def _setup_consignment() -> Consignment:
        result = Consignment("GR221000100")
        result.address.name = "Ryan Matfen"
        result.address.lines.append("Gillibrands Road")
        result.address.town = "Skelmersdale"
        result.address.post_code = "WN8 9TA"
        result.service.priority()
        result.client_name = "UPN"
        result.shipment_dates.collection = "03/10/2022"
        result.shipment_dates.delivery = "04/10/2022"

        return result

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

    def test_should_approve_priority_date(self):
        errors = self._validation.validate_dates_against_service()
        self.assertFalse(errors.incongruent_delivery_date)

    def test_should_highlight_priority_dates_error(self):
        self._setup_consignment.shipment_dates.delivery = "05/10/2022"

        errors = self._validation.validate_dates_against_service(
            self._setup_consignment)

        self.assertTrue(errors.incongruent_delivery_date)

    def test_should_highlight_economy_date_error(self):
        self._setup_consignment.service.economy()

        errors = self._validation.validate_dates_against_service(
            self._setup_consignment)

        self.assertTrue(errors.incongruent_delivery_date)

    def test_should_approve_economy_date(self):
        self._setup_consignment.service.economy()
        self._setup_consignment.shipment_dates.delivery = "05/10/2022"

        errors = self._validation.validate_dates_against_service(
            self._setup_consignment)

        self.assertFalse(errors.incongruent_delivery_date)

    def test_should_approve_economy_booked_date(self):
        self._setup_consignment.service.economy()
        self._setup_consignment.service.booked()
        self._setup_consignment.shipment_dates.delivery = "06/10/2022"

        errors = self._validation.validate_dates_against_service(
            self._setup_consignment)

        self.assertFalse(errors.incongruent_delivery_date)

    def test_should_highlight_economy_booked_date_error(self):
        self._setup_consignment.service.economy()
        self._setup_consignment.service.clear_booked_service()
        self._setup_consignment.shipment_dates.delivery = "06/10/2022"

        errors = self._validation.validate_dates_against_service(
            self._setup_consignment)

        self.assertTrue(errors.incongruent_delivery_date)

    def _tail_lift_errors_from_instruction(
            self, instruction: str) -> ConsignmentErrors:
        self._setup_consignment.delivery_instructions.clear()
        self._setup_consignment.delivery_instructions.append(instruction)

        return self._validation.validate_tail_lift_error(self._setup_consignment)


if __name__ == '__main__':
    unittest.main()
