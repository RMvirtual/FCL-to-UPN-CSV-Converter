from enum import Enum, auto
from src.main.freight.services.interface.booked_service import BookedServiceInterface


class BookedService(BookedServiceInterface):
    class Options(Enum):
        NONE = auto()
        BOOK_IN = auto()
        BOOKED = auto()

    def __init__(self):
        self._option = self.Options.NONE

    def book_in(self) -> None:
        self._option = self.Options.BOOK_IN

    def booked(self) -> None:
        self._option = self.Options.BOOKED

    def clear(self) -> None:
        self._option = self.Options.NONE

    def is_book_in(self) -> bool:
        return self._option == self.Options.BOOK_IN

    def is_booked(self) -> bool:
        return self._option == self.Options.BOOKED

    def is_not_required(self) -> bool:
        return self._option == self.Options.NONE

    def __bool__(self):
        return not self.is_not_required()

    def __eq__(self, other: BookedServiceInterface) -> bool:
        check_callbacks = {
            self.Options.NONE: other.is_not_required,
            self.Options.BOOK_IN: other.is_book_in,
            self.Options.BOOKED: other.is_booked
        }

        return check_callbacks[self._option]()
