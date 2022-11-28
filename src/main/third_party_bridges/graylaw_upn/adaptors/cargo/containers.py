from src.main.freight.cargo.container.interface import CargoReading
from src.main.freight.cargo.entries.interface import CargoEntry
from src.main.freight.cargo.packages.types.interface import PackageType
from src.main.upn.freight.cargo.container.container import UPNCargo


class UPNCargoAdaptor(CargoReading):
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

    def index_by_package_type(self, package_type: PackageType) -> CargoEntry:
        ...

    @property
    def total_weight(self) -> float:
        return self._cargo.total_weight
