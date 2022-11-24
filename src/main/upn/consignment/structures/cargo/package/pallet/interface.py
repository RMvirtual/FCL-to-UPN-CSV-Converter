from __future__ import annotations
from abc import ABC, abstractmethod
import copy
import dataclasses


class UPNPalletReading(ABC):
    @property
    @abstractmethod
    def size(self) -> str:
        ...

    @property
    @abstractmethod
    def type(self) -> str:
        ...

    def __eq__(self, other: UPNPalletReading):
        ...


@dataclasses.dataclass
class UPNPalletFields:
    type: str = ""
    size: str = ""
    type_constraints: list[str] = dataclasses.field(default=list[str])
    size_constraints: list[str] = dataclasses.field(default=list[str])


class UPNPallet(UPNPalletReading):
    @abstractmethod
    def __init__(self, pallet_fields: UPNPalletFields):
        self._type_constraints = pallet_fields.type_constraints
        self._size_constraints = pallet_fields.size_constraints
        self._type = pallet_fields.type
        self._size = pallet_fields.size

    @property
    def size(self) -> str:
        return self._size

    @size.setter
    def size(self, new_size: str) -> None:
        self._size = new_size

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, new_type: str) -> None:
        self._type = new_type

    @property
    def sizes(self) -> list[str]:
        return copy.deepcopy(self._size_constraints)

    @property
    def types(self) -> list[str]:
        return copy.deepcopy(self._type_constraints)

    def __eq__(self, other: UPNPalletReading) -> bool:
        return self.size == other.size and self.type == other.type
