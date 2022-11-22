from src.main.graylaw.cargo.container import interface
from src.main.graylaw.cargo.container.model import CargoModel
from src.main.graylaw.cargo.entries.interface import CargoEntry
from src.main.graylaw.cargo.packages.types.interface import PackageType


class Cargo(interface.Cargo):
    def __init__(self):
        self._model = CargoModel()

    def add(self, entry: CargoEntry) -> None:
        self._model.add(entry)

    def clear(self) -> None:
        self._model.clear()

    def index_by_package_type(self, package_type: PackageType) -> CargoEntry:
        return self._model.index_by_package_type(package_type)

    def __contains__(self, entry: CargoEntry) -> bool:
        return self._model.contains(entry)

    def __iter__(self):
        return self._model.__iter__()

    def __getitem__(self, index: int) -> CargoEntry:
        return self._model[index]

    def __len__(self) -> int:
        return len(self._model)
