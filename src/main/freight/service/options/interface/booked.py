from __future__ import annotations
from abc import abstractmethod
from src.main.freight.service.options.interface.optional import OptionalService


class BookedService(OptionalService):
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
    def __eq__(self, other: BookedService) -> bool:
        ...
