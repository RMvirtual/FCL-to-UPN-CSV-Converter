import csv


def read(src_path: str) -> list[list[str]]:
    with open(src_path, newline='') as csv_file:
        reader = csv.reader(csv_file, delimiter=',', quotechar='"')
        csv_readings = []

        for row in reader:
            csv_readings.append(row)

    return csv_readings

