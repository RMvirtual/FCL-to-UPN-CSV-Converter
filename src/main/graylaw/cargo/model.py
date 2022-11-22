from src.main.graylaw.cargo.entries.interface import CargoEntry
from src.main.graylaw.cargo.packages.types.interface import PackageType


class Cargo:
    def __init__(self):
        self._entries: list[CargoEntry] = []

    def add(self, entry: CargoEntry) -> None:
        self._combine(entry) if entry in self else self._add(entry)

    def _add(self, entry: CargoEntry) -> None:
        self._entries.append(entry)

    def _combine(self, new_entry: CargoEntry):
        self.entry_by_package_type(new_entry.package_type).__iadd__(new_entry)

    def clear(self) -> None:
        self._entries.clear()

    def contains(self, entry: CargoEntry) -> bool:
        self._raise_exception_if_type_not_cargo_entry(entry)

        return bool(self._matching_entries(entry.package_type))

    def entry_by_package_type(self, package_type: PackageType) -> CargoEntry:
        matching_entries = self._matching_entries(package_type)

        return matching_entries.pop() if matching_entries else None

    def _matching_entries(self, package_type: PackageType) -> list[CargoEntry]:
        return list(filter(
            lambda entry: entry.package_type == package_type, self._entries))

    def __contains__(self, entry: CargoEntry) -> bool:
        return self.contains(entry)

    def __iter__(self):
        return self._entries.__iter__()

    def __getitem__(self, index: int) -> CargoEntry:
        return self._entries[index]

    def __len__(self) -> int:
        return len(self._entries)

    @staticmethod
    def _raise_exception_if_type_not_cargo_entry(entry: any) -> None:
        if not isinstance(entry, CargoEntry):
            raise TypeError("Incorrect containing type to check for.")