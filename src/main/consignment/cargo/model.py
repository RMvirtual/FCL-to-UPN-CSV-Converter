from src.main.consignment.cargo.entry import CargoEntry


class Cargo:
    def __init__(self):
        self._entries: list[CargoEntry] = []

    def add(self, new_entry: CargoEntry) -> None:
        for entry in self._entries:
            if entry == new_entry:
                entry += new_entry

                return

        self._entries.append(new_entry)

    def __iter__(self):
        return self._entries.__iter__()

    def __getitem__(self, index: int) -> CargoEntry:
        return self._entries[index]

    def __len__(self) -> int:
        return len(self._entries)
