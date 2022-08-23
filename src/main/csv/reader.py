import csv


def read(src_path: str):
    with open(src_path, newline='') as csv_file:
        reader = csv.reader(csv_file, delimiter=',', quotechar='"')
        csv_reading = CsvReading()

        for row in reader:
            csv_reading.add(row)

    return csv_reading


class CsvReading:
    def __init__(self):
        self._rows = []

    def add(self, row: list[str]):
        self._rows.append(row)

    def row(self, index: int):
        return self._rows[index]

    def number_of_rows(self):
        return len(self._rows)

