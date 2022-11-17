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
