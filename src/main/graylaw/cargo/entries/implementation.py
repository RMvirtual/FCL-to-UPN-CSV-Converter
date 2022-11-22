from src.main.graylaw.cargo.packages.types.interface import PackageType
from src.main.graylaw.cargo.entries import interface
from src.main.graylaw.cargo.entries.model import CargoEntryModel


class CargoEntry(interface.CargoEntry):
    def __init__(self, package: PackageType, quantity: int, weight: float):
        self._model = CargoEntryModel(package, quantity, weight)

    @property
    def package_type(self) -> PackageType:
        return self._model.package_type

    @property
    def quantity(self) -> int:
        return self._model.quantity

    @quantity.setter
    def quantity(self, new_quantity: int) -> None:
        self._model.quantity = new_quantity

    @property
    def weight(self) -> float:
        return self._model.weight

    @weight.setter
    def weight(self, new_weight: float) -> None:
        self._model.weight = new_weight

    def set_totals(self, quantity: int, weight: float) -> None:
        self._model.set_totals(quantity, weight)

    def __eq__(self, other: interface.CargoEntry) -> bool:
        return self._model.__eq__(other)

    def __iadd__(self, other: interface.CargoEntry) -> interface.CargoEntry:
        return self._model.__iadd__(other)
