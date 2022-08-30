from src.main.freight.cargo.entry import CargoEntry
from src.main.freight.cargo.types import PackageType


class Cargo:
    def __init__(self):
        self._entries: list[CargoEntry] = []

    def add(self, new_entry: CargoEntry) -> None:
        existing_entry = self.entry_by_package_type(new_entry.package_type)

        if existing_entry:
            existing_entry += new_entry

        else:
            self._entries.append(new_entry)

    def entry_by_package_type(self, package_type: PackageType) -> CargoEntry:
        matching_cargo_entry = None

        for entry in self._entries:
            if entry.package_type == package_type:
                matching_cargo_entry = entry

                break

        return matching_cargo_entry

    def __iter__(self):
        return self._entries.__iter__()

    def __getitem__(self, index: int) -> CargoEntry:
        return self._entries[index]

    def __len__(self) -> int:
        return len(self._entries)
