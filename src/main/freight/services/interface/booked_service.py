from __future__ import annotations
from abc import ABC, abstractmethod


class BookedServiceInterface(ABC):
    @abstractmethod
    def book_in(self) -> None:
        ...

    @abstractmethod
    def booked(self) -> None:
        ...

    @abstractmethod
    def is_book_in(self) -> bool:
        ...

    @abstractmethod
    def is_booked(self) -> bool:
        ...

    @abstractmethod
    def is_not_required(self) -> bool:
        ...

    @abstractmethod
    def __bool__(self):
        ...

    @abstractmethod
    def __eq__(self, other: BookedServiceInterface) -> bool:
        ...
