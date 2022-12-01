from abc import ABC, abstractmethod


class MainServiceInterface(ABC):
    @abstractmethod
    def economy(self) -> None:
        ...

    @abstractmethod
    def next_day(self) -> None:
        ...

    @abstractmethod
    def is_economy(self) -> bool:
        ...

    @abstractmethod
    def is_next_day(self) -> bool:
        ...
