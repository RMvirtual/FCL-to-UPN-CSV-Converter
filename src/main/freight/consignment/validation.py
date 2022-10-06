import dataclasses
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
        pass

    def validate(self, consignment: Consignment) -> ConsignmentErrors:
        return ConsignmentErrors()
