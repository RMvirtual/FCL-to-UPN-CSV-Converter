from src.main.csv.reader import read as read_csv
from src.main.consignment.consignment import Consignment


def read(csv_path: str, ignore_headers: bool = False) \
        -> dict[str, Consignment]:
    csv_rows = read_csv(src_path=csv_path, ignore_headers=ignore_headers)
    fcl_format = FclCsvFormat()

    return fcl_format.parse(csv_rows)


class FclCsvFormat:
    """Interprets a list of strings as a UPNEDIIMP FCL CSV export."""

    def __init__(self):
        self._consignments: dict[str, Consignment] = {}

    def parse(self, csv_rows: list[list[str]]) -> dict[str, Consignment]:
        self._consignments.clear()

        for row in csv_rows:
            self._parse(row)

        return self._consignments

    def _parse(self, csv_row: list[str]) -> None:
        reference = csv_row[7]

        if reference in self._consignments:
            self._append_consignment(csv_row)

        else:
            self._new_consignment(csv_row)

    def _append_consignment(self, csv_row: list[str]) -> None:
        pass

    def _new_consignment(self, csv_row: list[str]) -> None:
        consignment = Consignment()
        consignment.reference = csv_row[7]

        self._consignments[consignment.reference] = consignment



