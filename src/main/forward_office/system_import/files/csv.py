from src.main.csv.reader import read as read_csv
from src.main.consignment.consignment import Consignment
from src.main.consignment_import.parser.consignment import ConsignmentParser


def read(
        csv_path: str, fields_to_indexes: dict[str, int],
        ignore_headers: bool = False) -> dict[str, Consignment]:
    csv_rows = read_csv(
        src_path=csv_path,
        ignore_headers=ignore_headers
    )

    parser = ConsignmentParser(fields_to_indexes)

    return parser.parse(csv_rows)
