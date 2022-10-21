import dataclasses
from src.main.freight.consignment.model import Consignment


@dataclasses.dataclass
class ConsignmentImportReport:
    consignments: dict[str, Consignment] = dataclasses.field(
        default_factory=dict[str, Consignment])

    errors: list[str] = dataclasses.field(default_factory=list[str])
    advisories: list[str] = dataclasses.field(default_factory=list[str])
