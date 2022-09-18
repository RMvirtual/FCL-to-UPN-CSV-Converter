from src.main.csv.reader import read as read_csv
from src.main.freight.consignment.consignment import Consignment
from src.main.forward_office.dashboard.export.parser.consignment \
    import ConsignmentParser


def read(
        csv_path: str, field_indexes: dict[str, int],
        ignore_headers: bool = False) -> dict[str, Consignment]:
    csv_rows = read_csv(
        src_path=csv_path,
        ignore_headers=ignore_headers
    )

    parser = ConsignmentParser(field_indexes)

    return parser.parse(csv_rows)
