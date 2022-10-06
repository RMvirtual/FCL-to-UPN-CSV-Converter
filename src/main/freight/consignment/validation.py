import dataclasses
import re
from src.main.freight.consignment.model import Consignment


@dataclasses.dataclass
class ConsignmentErrors:
    incongruent_delivery_date: bool = False
    tail_lift_advisory: bool = False
    priority_code_advisory: bool = False
    missing_weight: bool = False
    missing_package_type: bool = False
    missing_quantity: bool = False
    missing_minimum_address_details: bool = False

    def __bool__(self):
        return True in dataclasses.fields(self)


class ConsignmentValidationStrategy:
    def __init__(self):
        self._initialise_tail_lift_patterns()

    def _initialise_tail_lift_patterns(self):
        patterns = (
            "(tail lift|t/lift|t-lift|tail-lift| tl |tl | tl|t/l|t/l | t/l| "
            "t/l )"
        )

        self._tail_lift_patterns = re.compile(patterns, flags=re.I)

    def validate(self, consignment: Consignment) -> ConsignmentErrors:
        return ConsignmentErrors()

    def validate_tail_lift_error(
            self, consignment: Consignment) -> ConsignmentErrors:
        has_tail_lift_mention = False
        instructions = consignment.delivery_instructions

        for instruction in instructions:
            if re.search(self._tail_lift_patterns, instruction):
                has_tail_lift_mention = True

        errors = ConsignmentErrors()
        errors.tail_lift_advisory = has_tail_lift_mention

        return errors
