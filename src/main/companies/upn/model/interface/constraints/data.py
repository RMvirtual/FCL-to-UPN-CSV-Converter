from abc import ABC, abstractmethod


class DataConstraint(ABC):
    @property
    @abstractmethod
    def type(self) -> type:
        ...

    @property
    @abstractmethod
    def values(self) -> list[any]:
        ...
