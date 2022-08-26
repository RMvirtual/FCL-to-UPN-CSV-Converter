import csv


def read(src_path: str, ignore_headers: bool = False) -> list[list[str]]:
    with open(src_path, newline='') as csv_file:
        reader = csv.reader(csv_file, delimiter=',', quotechar='"')
        csv_readings = []

        starting_index = 1 if ignore_headers else 0

        for row in reader:
            reading = row
            csv_readings.append(reading)

    return csv_readings[starting_index:]

