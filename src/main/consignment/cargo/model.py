from src.main.consignment.cargo.entry import CargoEntry


class Cargo:
    def __init__(self):
        self._entries: list[CargoEntry] = []

    def add(self, new_entry: CargoEntry) -> None:
        for entry in self._entries:
            if entry.pallet_type.__class__ is new_entry.pallet_type.__class__:
                entry.total_weight += new_entry.total_weight
                entry.number_of_pallets += new_entry.number_of_pallets

                return

        self._entries.append(new_entry)

    def __iter__(self):
        return self._entries.__iter__()

    def __getitem__(self, index: int) -> CargoEntry:
        return self._entries[index]

    def __len__(self) -> int:
        return len(self._entries)
