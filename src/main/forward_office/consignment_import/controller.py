import dataclasses
from src.main.freight.consignment.model import Consignment


@dataclasses.dataclass
class ConsignmentImportReport:
    consignments: dict[str, Consignment] = dataclasses.field(
        default_factory=dict[str, Consignment])

    errors: list[str] = dataclasses.field(default_factory=list[str])
    advisories: list[str] = dataclasses.field(default_factory=list[str])


class FclImportController:
    def __init__(self, import_format):
        self._import_format = import_format

    def import_consignments(
            self, consignments: list[list[str]]) -> ConsignmentImportReport:
        ...

        return ConsignmentImportReport()



