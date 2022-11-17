from __future__ import annotations
from abc import ABC, abstractmethod


class OversizeOption(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @property
    @abstractmethod
    def multiplier(self) -> float:
        ...

    def __eq__(self, other: OversizeOption) -> bool:
        return self.name == other.name and self.multiplier == other.multiplier
