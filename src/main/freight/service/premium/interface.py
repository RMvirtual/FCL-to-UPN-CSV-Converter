from __future__ import annotations
from abc import ABC, abstractmethod


class PremiumServiceInterface(ABC):
    @abstractmethod
    def am(self) -> None:
        ...

    @abstractmethod
    def pre_10am(self) -> None:
        ...

    @abstractmethod
    def timed(self) -> None:
        ...

    @abstractmethod
    def clear(self) -> None:
        ...

    @abstractmethod
    def is_am(self) -> bool:
        ...

    @abstractmethod
    def is_pre_10am(self) -> bool:
        ...

    @abstractmethod
    def is_timed(self) -> bool:
        ...

    @abstractmethod
    def is_not_required(self) -> bool:
        ...

    @abstractmethod
    def __bool__(self):
        ...

    @abstractmethod
    def __eq__(self, other: PremiumServiceInterface) -> bool:
        ...
