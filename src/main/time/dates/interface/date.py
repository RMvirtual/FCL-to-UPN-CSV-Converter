from __future__ import annotations
from abc import ABC, abstractmethod


class DateInterface(ABC):
    @property
    @abstractmethod
    def day(self) -> int:
        ...

    @property
    @abstractmethod
    def month(self) -> int:
        ...

    @property
    @abstractmethod
    def year(self) -> int:
        ...

    @abstractmethod
    def __sub__(self, other: DateInterface) -> int:
        ...

    @abstractmethod
    def __eq__(self, other: DateInterface) -> bool:
        ...

    @abstractmethod
    def __lt__(self, other: DateInterface) -> bool:
        ...

    @abstractmethod
    def __le__(self, other: DateInterface) -> bool:
        ...

    @abstractmethod
    def __ge__(self, other: DateInterface) -> bool:
        ...

    @abstractmethod
    def __gt__(self, other: DateInterface) -> bool:
        ...
