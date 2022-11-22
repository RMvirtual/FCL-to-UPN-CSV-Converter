from src.main.upn.consignment.structures.cargo import UPNCargo
from src.main.graylaw.cargo.container.interface import Cargo
from src.main.graylaw.cargo.entries.interface import CargoEntry
from src.main.graylaw.cargo.packages.types.interface import PackageType


class UPNCargoAdaptor(Cargo):
    """Class for adapting a UPN Cargo structure into a Graylaw Cargo
    structure.
    """
    def __init__(self, upn_cargo: UPNCargo):
        self._cargo = upn_cargo

    def __contains__(self, entry: CargoEntry) -> bool:
        ...

    def __iter__(self):
        ...

    def __getitem__(self, index: int) -> CargoEntry:
        ...

    def __len__(self) -> int:
        return len(self._cargo.pallets)

    def add(self, entry: CargoEntry) -> None:
        ...

    def clear(self) -> None:
        ...

    def index_by_package_type(self, package_type: PackageType) -> CargoEntry:
        ...
