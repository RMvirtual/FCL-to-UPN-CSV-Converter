from dataclasses import dataclass

from src.main.csv.reader import read as read_csv
from src.main.freight.consignment.consignment import Consignment
from src.main.forward_office.dashboard.export.parser.consignment \
    import ConsignmentParser


@dataclass
class ReadParameters:
    dashboard_format: dict[str, int]
    csv_path: str = ""
    ignore_headers: bool = False


def read(parameters: ReadParameters) -> dict[str, Consignment]:
    csv_rows = read_csv(
        src_path=parameters.csv_path,
        ignore_headers=parameters.dashboard_format
    )

    parser = ConsignmentParser(parameters.dashboard_format)

    return parser.parse(csv_rows)
