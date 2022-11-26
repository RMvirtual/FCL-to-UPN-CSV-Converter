import functools
from src.main.freight.cargo.entries.interface import CargoEntry
from src.main.freight.cargo.packages.types.interface import PackageType
from src.main.freight.cargo.container import assertions


class CargoModel:
    def __init__(self):
        self._entries: list[CargoEntry] = []

    def add(self, entry: CargoEntry) -> None:
        self._combine(entry) if self.contains(entry) else self._add(entry)

    def contains(self, entry: CargoEntry) -> bool:
        assertions.assert_type_is_cargo_entry(entry)

        return bool(self._matching_entries(entry.package_type))

    def index_by_package_type(self, package_type: PackageType) -> CargoEntry:
        matching_entries = self._matching_entries(package_type)

        return matching_entries.pop() if matching_entries else None

    def clear(self) -> None:
        self._entries.clear()

    @property
    def total_weight(self) -> float:
        return functools.reduce(
            lambda entry_1, entry_2: entry_1.weight + entry_2.weight,
            self._entries
        )

    def _add(self, entry: CargoEntry) -> None:
        self._entries.append(entry)

    def _combine(self, new_entry: CargoEntry):
        self.index_by_package_type(new_entry.package_type).__iadd__(new_entry)

    def _matching_entries(self, package_type: PackageType) -> list[CargoEntry]:
        return list(filter(
            lambda entry: entry.package_type == package_type, self._entries))

    def __contains__(self, entry: CargoEntry) -> bool:
        return self.contains(entry)

    def __iter__(self) -> None:
        return self._entries.__iter__()

    def __getitem__(self, index: int) -> CargoEntry:
        return self._entries[index]

    def __len__(self) -> int:
        return len(self._entries)

