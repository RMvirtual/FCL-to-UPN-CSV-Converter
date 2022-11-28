from __future__ import annotations
from abc import abstractmethod
import copy
import dataclasses
from src.main.companies.upn.api.interfaces.pallets.upn_pallet import (
    UPNPalletInterface, UPNPalletReading)


@dataclasses.dataclass
class UPNPalletFields:
    type: str = ""
    size: str = ""
    type_constraints: list[str] = dataclasses.field(default=list[str])
    size_constraints: list[str] = dataclasses.field(default=list[str])


class AbstractUPNPallet(UPNPalletInterface):
    """Abstraction of a UPN base pallet class."""

    @abstractmethod
    def __init__(self, pallet_fields: UPNPalletFields):
        self._type_constraints = pallet_fields.type_constraints
        self._size_constraints = pallet_fields.size_constraints
        self._type = pallet_fields.type
        self._size = pallet_fields.size

    @property
    def size(self, **kwargs) -> str:
        # Has **kwargs due to IDE ERROR.
        return self._size

    @size.setter
    def size(self, new_size: str) -> None:
        self._raise_exception_if_invalid_size(new_size)
        self._size = new_size

    @property
    def type(self, **kwargs) -> str:
        return self._type

    @type.setter
    def type(self, new_type: str) -> None:
        self._raise_exception_if_invalid_type(new_type)
        self._type = new_type

    @property
    def size_constraints(self) -> list[str]:
        return copy.deepcopy(self._size_constraints)

    @property
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