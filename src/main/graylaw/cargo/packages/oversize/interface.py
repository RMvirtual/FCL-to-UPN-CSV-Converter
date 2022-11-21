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

    @abstractmethod
    def __eq__(self, other: OversizeOption):
        ...


class OversizeOptions(ABC):
    @property
    @abstractmethod
    def default(self) -> OversizeOption:
        ...

    @property
    @abstractmethod
    def values(self) -> list[OversizeOption]:
        ...

    @property
    @abstractmethod
    def selected(self) -> OversizeOption:
        ...

    @selected.setter
    @abstractmethod
    def selected(self, option: OversizeOption) -> None:
        ...

    @abstractmethod
    def select(self, option_name: str) -> None:
        ...

    @abstractmethod
    def __getitem__(self, option_name: str) -> OversizeOption:
        ...

    @abstractmethod
    def __contains__(self, item: OversizeOption) -> bool:
        ...

    @abstractmethod
    def __eq__(self, other: OversizeOptions) -> bool:
        ...
