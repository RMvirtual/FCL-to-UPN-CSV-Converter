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
