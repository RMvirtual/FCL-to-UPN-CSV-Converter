from __future__ import annotations
from abc import abstractmethod
import copy
import dataclasses
from src.main.upn.consignment.cargo.package.pallet.interface import (
    UPNPallet, UPNPalletReading)


@dataclasses.dataclass
class UPNPalletFields:
    type: str = ""
    size: str = ""
    type_constraints: list[str] = dataclasses.field(default=list[str])
    size_constraints: list[str] = dataclasses.field(default=list[str])


class AbstractUPNPallet(UPNPallet):
    """Abstraction of a UPN base pallet class."""

    @abstractmethod
    def __init__(self, pallet_fields: UPNPalletFields):
        self._type_constraints = pallet_fields.type_constraints
        self._size_constraints = pallet_fields.size_constraints
        self._type = pallet_fields.type
        self._size = pallet_fields.size

    @UPNPallet.size.getter
    def size(self) -> str:
        return self._size

    @UPNPallet.size.setter
    def size(self, new_size: str) -> None:
        self._raise_exception_if_invalid_size(new_size)
        self._size = new_size

    @UPNPallet.type.getter
    def type(self) -> str:
        return self._type

    @UPNPallet.type.setter
    def type(self, new_type: str) -> None:
        self._raise_exception_if_invalid_type(new_type)
        self._type = new_type

    @UPNPallet.size_constraints.getter
    def size_constraints(self) -> list[str]:
        return copy.deepcopy(self._size_constraints)

    @UPNPallet.type_constraints.getter
    def type_constraints(self) -> list[str]:
        return copy.deepcopy(self._type_constraints)

    def __eq__(self, other: UPNPalletReading) -> bool:
        return self.size == other.size and self.type == other.type

    def _raise_exception_if_invalid_type(self, type_name: str) -> None:
        if type_name not in self._type_constraints:
            raise ValueError(
                f"Type {type_name} is invalid. "
                f"Valid types are [{self._type_constraints}]."
            )

    def _raise_exception_if_invalid_size(self, size_name: str) -> None:
        if size_name not in self._size_constraints:
            raise ValueError(
                f"Size {size_name} is invalid. "
                f"Valid sizes are [{self._size_constraints}]"
            )
