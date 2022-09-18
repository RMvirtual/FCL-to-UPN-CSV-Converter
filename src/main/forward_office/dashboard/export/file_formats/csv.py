from src.main.csv.reader import read as read_csv
from src.main.freight.consignment.consignment import Consignment
from src.main.forward_office.dashboard.export.parser.consignment \
    import ConsignmentParser


class ReadParameters:
    def __init__(self):
        self.csv_path: str = ""
        self.field_indexes: dict[str, int] = {}
        self.ignore_headers: bool = False


def read(parameters: ReadParameters) -> dict[str, Consignment]:
    csv_rows = read_csv(
        src_path=parameters.csv_path,
        ignore_headers=parameters.field_indexes
    )

    parser = ConsignmentParser(parameters.field_indexes)

    return parser.parse(csv_rows)
