from src.main.consignment.cargo.entry import CargoEntry


class Cargo:
    def __init__(self):
        self._entry_lines: list[CargoEntry] = []

    def add(self, cargo_entry: CargoEntry) -> None:
        self._entry_lines.append(cargo_entry)

    def __iter__(self):
        return self._entry_lines.__iter__()

    def __getitem__(self, index: int) -> CargoEntry:
        return self._entry_lines[index]

