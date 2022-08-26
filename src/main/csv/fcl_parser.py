from src.main.csv.reader import read as read_csv
from src.main.consignment.consignment import Consignment


def read(csv_path: str, ignore_headers: bool = False) -> list[Consignment]:
    csv_rows = read_csv(src_path=csv_path, ignore_headers=ignore_headers)

    return csv_rows

