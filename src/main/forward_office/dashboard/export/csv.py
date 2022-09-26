from dataclasses import dataclass, field

from src.main.file_system.file_readers import csv_file
from src.main.freight.consignment.consignment import Consignment
from src.main.forward_office.dashboard.parser.reference \
    import ConsignmentParser


# noinspection PyClassHasNoInit
@dataclass
class ReadParameters:
    dashboard_format: dict[str, int] = field(default_factory=lambda: {})
    csv_path: str = ""
    ignore_headers: bool = False


def read(parameters: ReadParameters) -> dict[str, Consignment]:
    csv_rows = csv_file.read(
        src_path=parameters.csv_path,
        ignore_headers=parameters.dashboard_format
    )

    parser = ConsignmentParser(parameters.dashboard_format)

    return parser.parse(csv_rows)
