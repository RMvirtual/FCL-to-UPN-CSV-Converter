from __future__ import annotations

from abc import ABC, abstractmethod


class UPNPallet(ABC):
    @property
    @abstractmethod
    def size(self) -> str:
        """Size code."""
        ...

    @property
    @abstractmethod
    def type(self) -> str:
        """Type Code"""
        ...

    @size.setter
    @abstractmethod
    def size(self, new_size: str) -> None:
        """Sets the size code."""
        ...

    @type.setter
    @abstractmethod
    def type(self, new_type: str) -> None:
        """Sets the type code."""
        ...

    @property
    @abstractmethod
    def size_constraints(self) -> list[str]:
        """The list of valid size codes."""
        ...

    @property
    @abstractmethod
    def type_constraints(self) -> list[str]:
        """The list of valid type codes."""
        ...

    @abstractmethod
    def __eq__(self, other: UPNPallet):
        ...

